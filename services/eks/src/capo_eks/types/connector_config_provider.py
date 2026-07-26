"""Generated from Smithy shape ``com.amazonaws.eks#ConnectorConfigProvider``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ConnectorConfigProvider) -> str:
    return value


def deserialize_json(data: str) -> ConnectorConfigProvider:
    return cast(ConnectorConfigProvider, data)
