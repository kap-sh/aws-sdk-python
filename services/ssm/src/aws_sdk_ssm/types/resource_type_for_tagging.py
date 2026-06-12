"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceTypeForTagging``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ResourceTypeForTagging: TypeAlias = Literal[
    "Document",
    "ManagedInstance",
    "MaintenanceWindow",
    "Parameter",
    "PatchBaseline",
    "OpsItem",
    "OpsMetadata",
    "Automation",
    "Association",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Document",
        "ManagedInstance",
        "MaintenanceWindow",
        "Parameter",
        "PatchBaseline",
        "OpsItem",
        "OpsMetadata",
        "Automation",
        "Association",
    )
)


def serialize_aws_json_1_1(value: ResourceTypeForTagging) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceTypeForTagging:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceTypeForTagging value: {data!r}")
    return cast(ResourceTypeForTagging, data)
