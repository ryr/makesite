GIT_PROJECT_TEMP_DIR=/tmp/$!project_name!$$!branch!$
GIT_PROJECT_DIR=$!deploy_dir!$/source

cp -r $GIT_PROJECT_DIR $GIT_PROJECT_TEMP_DIR
cd $GIT_PROJECT_TEMP_DIR && git reset --hard HEAD && git pull