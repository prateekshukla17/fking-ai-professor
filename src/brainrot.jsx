import { useState } from 'react';

export default function Brainrot() {
  const [topic, setTopic] = useState('');
  const [audioSrc, setAudioSrc] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateLecture = async () => {
    if (!topic.trim()) return alert('Fucking type something bruh.');
    setLoading(true);
    setAudioSrc(null);

    try {
      const res = await fetch('http://127.0.0.1:8000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic }),
      });

      if (!res.ok) throw new Error('Generation failed bruh');

      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      setAudioSrc(url);
    } catch (err) {
      alert('Shit broke: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>🧠 BRAINROT ACADEMY</h1>
      <p>Enter a topic and get mentally violated by an AI professor.</p>

      <div>
        <input
          type='text'
          placeholder='e.g. Recursion'
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
        <button onClick={generateLecture}>Generate</button>
      </div>

      {loading && <div>GENERATING THIS UNHINGED MASTERPIECE...</div>}

      {audioSrc && !loading && (
        <div className='mt-8'>
          <audio controls autoPlay src={audioSrc} />
        </div>
      )}
    </div>
  );
}
