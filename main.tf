resource "aws_ecs_cluster" "c1" {
    name = "xyz"
    setting {
        name = "containerInsights"
        value = "enabled"
    }
}

resource "aws_ecs_cluster" "fail" {
    name = "xyz1"
    setting {
        name = "containerInsights"
        value = "enabled"
    }
}