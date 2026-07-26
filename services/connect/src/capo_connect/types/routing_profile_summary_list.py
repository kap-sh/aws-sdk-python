"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.routing_profile_summary

RoutingProfileSummaryList: TypeAlias = list[
    "capo_connect.types.routing_profile_summary.RoutingProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileSummaryList) -> list:
    import capo_connect.types.routing_profile_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.routing_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutingProfileSummaryList:
    import capo_connect.types.routing_profile_summary

    out: RoutingProfileSummaryList = []
    for item in data:
        out.append(capo_connect.types.routing_profile_summary.deserialize_json(item))
    return out
