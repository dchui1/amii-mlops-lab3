if [[ ../../model.pkl -nt ../../webapp/model.pkl ]] || ! [ -f ../../webapp/model.pkl] ; then
  echo "Model is newer, deploying"
  cp ../../model.pkl ../../webapp/
fi