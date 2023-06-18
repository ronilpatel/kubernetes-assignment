
provider "google" {
  credentials = file("./key.json")
  project     = "assignment-kubernetes-390016"
  region      = "us-east1"
}

resource "google_container_cluster" "my_cluster" {
  name               = "ronils-cluster"
  location           = "us-east1"
  initial_node_count = 1


  master_auth {
    client_certificate_config {
      issue_client_certificate = false
    }
  }
}