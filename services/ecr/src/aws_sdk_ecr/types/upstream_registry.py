"""Generated from Smithy shape ``com.amazonaws.ecr#UpstreamRegistry``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ecr",
        "ecr-public",
        "quay",
        "k8s",
        "docker-hub",
        "github-container-registry",
        "azure-container-registry",
        "gitlab-container-registry",
        "chainguard",
    )
)


def serialize_aws_json_1_1(value: UpstreamRegistry) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpstreamRegistry:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpstreamRegistry value: {data!r}")
    return cast(UpstreamRegistry, data)
