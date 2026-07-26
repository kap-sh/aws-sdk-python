"""Generated from Smithy shape ``com.amazonaws.ecr#UpstreamRegistry``."""

from typing import Literal, TypeAlias, cast

UpstreamRegistry: TypeAlias = Literal[
    "ecr",
    "ecr-public",
    "quay",
    "k8s",
    "docker-hub",
    "github-container-registry",
    "azure-container-registry",
    "gitlab-container-registry",
    "chainguard",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpstreamRegistry) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpstreamRegistry:
    return cast(UpstreamRegistry, data)
