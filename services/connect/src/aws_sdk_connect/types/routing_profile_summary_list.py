"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_summary

RoutingProfileSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile_summary.RoutingProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileSummaryList) -> list:
    import aws_sdk_connect.types.routing_profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.routing_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutingProfileSummaryList:
    import aws_sdk_connect.types.routing_profile_summary

    out: RoutingProfileSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.routing_profile_summary.deserialize_json(item))
    return out
