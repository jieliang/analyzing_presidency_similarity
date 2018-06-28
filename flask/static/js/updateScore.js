function updateScore(){
  const theReview = document.getElementById('review_text').value;
  const outputElement = document.getElementById('output');
  if (theReview.length < 15) {
      outputElement.textContent = 'Need more text to provide review';
      return;
  }

  $.ajax({
    type: 'POST',
    contentType: "application/json; charset=utf-8",
    url: '/sentiment_score',
    async: true,
    data: JSON.stringify({
      review: theReview
    }),
    success: (response) => {
      outputElement.textContent = response.score;
      smile(response.score);
    },
    error: (response) => {
      outputElement.textContent = 'INVALID';
    }
  })
}
