"""Generated from Smithy shape ``com.amazonaws.location#GeoArnList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.geo_arn_v2

GeoArnList: TypeAlias = list["aws_sdk_location.types.geo_arn_v2.GeoArnV2"]


# --- restJson1 ser/de ---
def serialize_json(value: GeoArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> GeoArnList:
    return list(data)