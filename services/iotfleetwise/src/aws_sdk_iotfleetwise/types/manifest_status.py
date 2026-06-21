"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ManifestStatus``."""

from typing import Literal, TypeAlias, cast

ManifestStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAFT",
    "INVALID",
    "VALIDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManifestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ManifestStatus:
    return cast(ManifestStatus, data)
