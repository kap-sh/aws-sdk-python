"""Generated from Smithy shape ``com.amazonaws.directconnect#LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.location

LocationList: TypeAlias = list["capo_direct_connect.types.location.Location"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationList) -> list:
    import capo_direct_connect.types.location

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.location.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationList:
    import capo_direct_connect.types.location

    out: LocationList = []
    for item in data:
        out.append(capo_direct_connect.types.location.deserialize_aws_json_1_1(item))
    return out
