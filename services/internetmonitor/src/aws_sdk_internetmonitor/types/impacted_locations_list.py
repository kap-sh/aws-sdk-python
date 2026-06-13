"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ImpactedLocationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.impacted_location

ImpactedLocationsList: TypeAlias = list[
    "aws_sdk_internetmonitor.types.impacted_location.ImpactedLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedLocationsList) -> list:
    import aws_sdk_internetmonitor.types.impacted_location

    out: list = []
    for item in value:
        out.append(aws_sdk_internetmonitor.types.impacted_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImpactedLocationsList:
    import aws_sdk_internetmonitor.types.impacted_location

    out: ImpactedLocationsList = []
    for item in data:
        out.append(
            aws_sdk_internetmonitor.types.impacted_location.deserialize_json(item)
        )
    return out
