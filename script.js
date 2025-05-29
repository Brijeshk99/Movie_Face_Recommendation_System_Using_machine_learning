document.getElementById('capture-btn').addEventListener('click', captureImage);

async function captureImage() {
    const video = document.getElementById('webcam');
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Here you would send the image to the backend for emotion detection
    // For demonstration, we'll just simulate emotion detection
    const detectedEmotion = simulateEmotionDetection();
    document.getElementById('emotion-display').innerText = `Detected Emotion: ${detectedEmotion}`;
    
    // Fetch movie recommendations based on detected emotion
    fetchMovieRecommendations(detectedEmotion);
}

function simulateEmotionDetection() {
    const emotions = ['Happy', 'Sad', 'Angry', 'Surprised', 'Neutral'];
    return emotions[Math.floor(Math.random() * emotions.length)];
}

function fetchMovieRecommendations(emotion) {
    const movieCardsContainer = document.getElementById('movie-cards');
    movieCardsContainer.innerHTML = ''; // Clear previous recommendations

    // Simulated movie recommendations based on emotion
    const movieRecommendations = {
        Happy: ['Movie A', 'Movie B', 'Movie C'],
        Sad: ['Movie D', 'Movie E', 'Movie F'],
        Angry: ['Movie G', 'Movie H', 'Movie I'],
        