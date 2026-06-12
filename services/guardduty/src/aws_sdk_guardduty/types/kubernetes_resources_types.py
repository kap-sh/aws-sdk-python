"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesResourcesTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PODS",
        "JOBS",
        "CRONJOBS",
        "DEPLOYMENTS",
        "DAEMONSETS",
        "STATEFULSETS",
        "REPLICASETS",
        "REPLICATIONCONTROLLERS",
    )
)


def serialize_json(value: KubernetesResourcesTypes) -> str:
    return value


def deserialize_json(data: str) -> KubernetesResourcesTypes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KubernetesResourcesTypes value: {data!r}")
    return cast(KubernetesResourcesTypes, data)
