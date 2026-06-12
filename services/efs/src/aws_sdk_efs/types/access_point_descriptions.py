"""Generated from Smithy shape ``com.amazonaws.efs#AccessPointDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.access_point_description

AccessPointDescriptions: TypeAlias = list[
    "aws_sdk_efs.types.access_point_description.AccessPointDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointDescriptions) -> list:
    import aws_sdk_efs.types.access_point_description

    out: list = []
    for item in value:
        out.append(aws_sdk_efs.types.access_point_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPointDescriptions:
    import aws_sdk_efs.types.access_point_description

    out: AccessPointDescriptions = []
    for item in data:
        out.append(aws_sdk_efs.types.access_point_description.deserialize_json(item))
    return out
