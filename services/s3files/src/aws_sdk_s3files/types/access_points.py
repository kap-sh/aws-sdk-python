"""Generated from Smithy shape ``com.amazonaws.s3files#AccessPoints``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_s3files.types.list_access_points_description

AccessPoints: TypeAlias = list["aws_sdk_s3files.types.list_access_points_description.ListAccessPointsDescription"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPoints) -> list:
    import aws_sdk_s3files.types.list_access_points_description
    out: list = []
    for item in value:
        out.append(aws_sdk_s3files.types.list_access_points_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPoints:
    import aws_sdk_s3files.types.list_access_points_description
    out: AccessPoints = []
    for item in data:
        out.append(aws_sdk_s3files.types.list_access_points_description.deserialize_json(item))
    return out