"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#fleetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.fleet_summary

fleetSummaries: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.fleet_summary.FleetSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: fleetSummaries) -> list:
    import aws_sdk_iotfleetwise.types.fleet_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.fleet_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> fleetSummaries:
    import aws_sdk_iotfleetwise.types.fleet_summary

    out: fleetSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.fleet_summary.deserialize_aws_json_1_0(item)
        )
    return out
