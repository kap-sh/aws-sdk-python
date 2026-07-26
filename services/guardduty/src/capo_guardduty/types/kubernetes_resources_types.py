"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesResourcesTypes``."""

from typing import Literal, TypeAlias, cast

KubernetesResourcesTypes: TypeAlias = Literal[
    "PODS",
    "JOBS",
    "CRONJOBS",
    "DEPLOYMENTS",
    "DAEMONSETS",
    "STATEFULSETS",
    "REPLICASETS",
    "REPLICATIONCONTROLLERS",
]


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesResourcesTypes) -> str:
    return value


def deserialize_json(data: str) -> KubernetesResourcesTypes:
    return cast(KubernetesResourcesTypes, data)
