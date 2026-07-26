"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Destinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.destination

Destinations: TypeAlias = list["capo_cloudtrail.types.destination.Destination"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Destinations) -> list:
    import capo_cloudtrail.types.destination

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.destination.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Destinations:
    import capo_cloudtrail.types.destination

    out: Destinations = []
    for item in data:
        out.append(capo_cloudtrail.types.destination.deserialize_aws_json_1_1(item))
    return out
