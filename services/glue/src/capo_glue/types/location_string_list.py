"""Generated from Smithy shape ``com.amazonaws.glue#LocationStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.location_string

LocationStringList: TypeAlias = list["capo_glue.types.location_string.LocationString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LocationStringList:
    return list(data)
