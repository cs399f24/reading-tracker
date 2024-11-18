INSTANCE_IP=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=readingtrackerdynamo" --query "Reservations[0].Instances[0].PublicIpAddress" --output text)

URL="http://$INSTANCE_IP:8080"

sed -i "s|^\([[:space:]]*\)const server = 'http://.*';|\1const server = '$URL';|" index.html

aws s3 cp index.html s3://reading-tracker
