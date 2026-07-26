"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeNetworkSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.describe_network_summary

__listOfDescribeNetworkSummary: TypeAlias = list[
    "capo_medialive.types.describe_network_summary.DescribeNetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeNetworkSummary) -> list:
    import capo_medialive.types.describe_network_summary

    out: list = []
    for item in value:
        out.append(capo_medialive.types.describe_network_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDescribeNetworkSummary:
    import capo_medialive.types.describe_network_summary

    out: __listOfDescribeNetworkSummary = []
    for item in data:
        out.append(capo_medialive.types.describe_network_summary.deserialize_json(item))
    return out
