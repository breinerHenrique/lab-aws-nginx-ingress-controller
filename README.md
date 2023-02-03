# Install Nginx Ingress Controller
helm upgrade --install nginx-controller-internal ingress-nginx/ingress-nginx -f k8s/values-nginx-ingress-controller.yaml -n kube-system

