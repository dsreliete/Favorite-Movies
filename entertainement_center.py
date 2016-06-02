import fresh_tomatoes
import movie 

toy_story = movie.Movie('Toy Story', 'Woody, um cowboy de pano é o brinquedo ' +
                        'favorito de Andy, mas quando Andy e outros ' +
                        'humanos não estão olhando Andy e demais brinquedos ganham vida.',
                        'http://br.web.img3.acsta.net/medias/nmedia/18/91/05/36/20127436.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
#print(toy_story.storyline)

bela_fera = movie.Movie('A Bela e a Fera', 'Em uma pequena aldeia da França vive Belle, uma jovem inteligente que é ' +
                        'considerada estranha pelo moradores da localidade, e seu pai, Maurice, um inventor que é ' +
                        'visto como um louco. Ela é cortejada por Gaston, que quer casar com ela. Mas apesar de todas ' +
                        'as jovens do lugarejo o acharem um homem bonito, Belle não o suporta, pois vê nele uma pessoa ' +
                        'primitiva e convencida. Quando o pai de Belle vai para uma feira demonstrar sua nova invenção, '+
                        'ele acaba se perdendo na floresta e é atacado por lobos. Desesperado, Maurice procura abrigo em ' +
                        'um castelo, mas acaba se tornando prisioneiro da Fera, o senhor do castelo, que na verdade é um ' +
                        'príncipe que foi amaldiçoado por uma feiticeira quando negou abrigo a ela. Quando Belle sente ' +
                        'que algo aconteceu ao seu pai vai à sua procura. Ela chega ao castelo e lá faz um acordo com ' +
                        'a Fera: se seu pai fosse libertado ela ficaria no castelo para sempre. A Fera concorda e todos os ' +
                        'moradores do castelo, que lá vivem e também foram transformados em objetos falantes, sentem que esta '+
                        'pode ser a chance do feitiço ser quebrado. Mas isto só acontecerá se a Fera amar alguém e esta pessoa ' +
                        'retribuir o seu amor, sendo que isto tem de ser rápido, pois quando a última pétala de uma rosa encantada ' +
                        'cair o feitiço não poderá ser mais desfeito.',
                        'http://vignette3.wikia.nocookie.net/disneyprincesas/images/9/9f/' +
                        'Poster_A_Bela_e_a_Fera.jpg/revision/latest?cb=20140718003506&path-prefix=pt-br',
                        'https://www.youtube.com/watch?v=MJiZxIIXhhk')
#print(bela_fera.title)

johnny_june = movie.Movie('Johnny e June', 'A história do cantor Johnny Cash (Joaquin Phoenix), desde sua juventude em' +
                          'uma fazenda de algodão até o início do sucesso em Memphis, onde gravou com Elvis Presley, ' +
                          'Johnny Lee Lewis e Carl Perkins. Sua personalidade marginal e a infância tumultuada fazem ' +
                          'com que Johnny entre em um caminho de auto-destruição, do qual apenas June Carter ' +
                          '(Reese Whiterspoon), o grande amor de sua vida, pode salvar.',
                          'https://yobotarate.files.wordpress.com/2008/07/johnny-e-june-poster07.jpg',
                          'https://www.youtube.com/watch?v=PYy0sfFwm4E')
#print(johnny_june.trailer_youtube_url)
#johnny_june.show_trailer()

madson_bridge = movie.Movie('As ponte de Madson','Após a morte de Francesca Johnson (Meryl Streep), uma proprietária ' +
                            'rural do interior do Iowa, seus filhos descobrem, através de cartas que a mãe deixou, do ' +
                            'forte envolvimento que ela teve com um fotógrafo (Clint Eastwood) da National Geographic, ' +
                            'quando a família se ausentou de casa por quatro dias. '+
                            'Estas revelações fazem os filhos questionarem seus próprios casamentos.',
                            'http://br.web.img3.acsta.net/medias/nmedia/18/90/90/74/20119562.jpg',
                            'https://www.youtube.com/watch?v=VDJBLEY2jrg')
#print(madson_bridge.poster_image_url)

movies = [toy_story, bela_fera, johnny_june, madson_bridge]
fresh_tomatoes.open_movies_page(movies)
print(movie.Movie.__doc__)




