"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#vehicleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.vehicle_summary

vehicleSummaries: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.vehicle_summary.VehicleSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: vehicleSummaries) -> list:
    import aws_sdk_iotfleetwise.types.vehicle_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.vehicle_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> vehicleSummaries:
    import aws_sdk_iotfleetwise.types.vehicle_summary

    out: vehicleSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.vehicle_summary.deserialize_aws_json_1_0(item)
        )
    return out
