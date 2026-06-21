"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceTypeForTagging``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ResourceTypeForTagging) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceTypeForTagging:
    return cast(ResourceTypeForTagging, data)
