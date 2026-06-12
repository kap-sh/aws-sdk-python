"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeNetworkSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.describe_network_summary

__listOfDescribeNetworkSummary: TypeAlias = list[
    "aws_sdk_medialive.types.describe_network_summary.DescribeNetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeNetworkSummary) -> list:
    import aws_sdk_medialive.types.describe_network_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.describe_network_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfDescribeNetworkSummary:
    import aws_sdk_medialive.types.describe_network_summary

    out: __listOfDescribeNetworkSummary = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.describe_network_summary.deserialize_json(item)
        )
    return out
