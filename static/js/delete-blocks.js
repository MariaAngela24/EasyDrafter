function deleteBlockTop (evt) {
	evt.preventDefault();

	$.ajax({
		url: "/delete-block-top",
		data: {'chart-id':$(this).val()},
		type: "POST",
		success: function(response) {
			console.log(response)
		},
		error: function(error) {
			console.log('error')
		}
	});
	$(this).closest('.saved-block').remove();
}

$('.delete-btn-top').on('click', deleteBlockTop);

function deleteBlockSkirt (evt) {
	evt.preventDefault();
	console.log("DELETE SKIRT")

	$.ajax({
		url: "/delete-block-skirt",
		data: {'chart-id':$(this).val()},
		type: "POST",
		success: function(response) {
			console.log(response)
		},
		error: function(error) {
			console.log('error')
		}
	});
	$(this).closest('.saved-block').remove();
}

$('.delete-btn-skirt').on('click', function() { console.log("pressed")})