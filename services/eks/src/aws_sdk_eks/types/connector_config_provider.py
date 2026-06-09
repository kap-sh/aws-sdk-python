"""Generated from Smithy shape ``com.amazonaws.eks#ConnectorConfigProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

ConnectorConfigProvider: TypeAlias = Literal[
    "EKS_ANYWHERE",
    "ANTHOS",
    "GKE",
    "AKS",
    "OPENSHIFT",
    "TANZU",
    "RANCHER",
    "EC2",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EKS_ANYWHERE",
        "ANTHOS",
        "GKE",
        "AKS",
        "OPENSHIFT",
        "TANZU",
        "RANCHER",
        "EC2",
        "OTHER",
    )
)


def serialize_json(value: ConnectorConfigProvider) -> str:
    return value


def deserialize_json(data: str) -> ConnectorConfigProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorConfigProvider value: {data!r}")
    return cast(ConnectorConfigProvider, data)
