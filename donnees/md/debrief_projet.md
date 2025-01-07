# Débriefing du projet de moteur de recommandation de films

## Points forts du projet
- **Apprentissage enrichissant** :  
  Découverte de nouveaux outils et techniques comme GitHub, le Machine Learning et Streamlit. Ces apprentissages ont permis de renforcer nos compétences techniques et notre capacité à travailler en équipe.
  
- **Ouverture à une culture cinématographique diversifiée** :  
  Le projet nous a plongés dans des univers cinématographiques méconnus, notamment ceux de l'Inde, du Japon et des films d'auteurs. Une belle opportunité pour sortir des productions classiques et explorer un cinéma moins conventionnel.

- **Vision large et authentique** :  
  Nous avons cherché à proposer un moteur de recommandation différent, avec une sélection de films qui va au-delà des standards hollywoodiens, adaptée à une clientèle cible (notamment senior) intéressée par des films d'auteurs et indépendants.

- **Collaboration d'équipe** :  
  Malgré les défis, notre équipe a su maintenir une bonne cohésion et surmonter ensemble les difficultés liées à l'implémentation et au débogage.

## Points faibles et difficultés rencontrées
- **Découverte tardive de nouvelles techniques** :  
  L'introduction du Machine Learning après nos premières analyses (études de marché et KPIs) nous a obligés à revenir en arrière pour adapter nos besoins. Cela a engendré une perte de temps significative.

- **Complexité de gestion des outils collaboratifs** :  
  L'utilisation de GitHub, essentielle au projet, a été une difficulté majeure. Nous avons dû apprendre à éviter des erreurs comme écraser le travail des autres et à résoudre des conflits sur les branches.

- **Limites techniques de Streamlit** :  
  Développer une interface utilisateur intuitive tout en gérant les nombreux bugs imprévus s'est révélé être un défi constant, en particulier dans les dernières étapes du projet.

- **Critères de sélection trop larges** :  
  Initialement, notre base de données contenait environ 300 000 films, mais nous avons réduit ce nombre à 78 000 pour correspondre à notre cible. Malgré cela, des critères encore trop inclusifs (par exemple, notes > 7/10 ou ≥ 300 votes) ont parfois mené à des résultats qui pouvaient perturber l'utilisateur.

## Pistes d'amélioration
1. **Optimisation des critères de l'algorithme** :  
   - Réhausser la barre des notes minimales (par exemple, > 8/10).  
   - Augmenter le seuil des votes (par exemple, à partir de 500 ou 1000 votes).  
   - Affiner encore la sélection pour améliorer la pertinence des recommandations.

2. **Gestion des outils collaboratifs** :  
   - Renforcer les bonnes pratiques sur GitHub (création de branches claires, documentation des commits).  
   - Organiser des sessions régulières pour s'assurer de la synchronisation entre les membres de l'équipe.

3. **Streamlit et interfaces utilisateur** :  
   - Tester plus tôt l'interface pour identifier les limites techniques.  
   - Anticiper des sessions de débogage avant les phases critiques.

4. **Base de données et diversité culturelle** :  
   - Explorer davantage les cinémas locaux pour enrichir la base de données.  
   - Continuer à intégrer des films d'auteurs et indépendants tout en affinant la sélection pour rester cohérent avec la cible.

5. **Planification du projet** :  
   - Allouer plus de temps à la découverte et à la maîtrise des outils en début de projet.  
   - Prendre en compte les ajustements nécessaires lorsque de nouvelles techniques sont introduites en cours de route.

## Conclusion
Ce projet, bien que complexe, a été une expérience très enrichissante. Nous avons appris non seulement à manipuler des outils techniques, mais aussi à travailler sur un projet avec une vision authentique et une ouverture culturelle. Ce moteur de recommandation, bien qu'imparfait, reflète notre ambition de sortir des sentiers battus pour offrir un outil original et pertinent.