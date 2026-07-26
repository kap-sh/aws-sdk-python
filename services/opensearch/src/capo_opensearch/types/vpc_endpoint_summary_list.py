"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_summary

VpcEndpointSummaryList: TypeAlias = list[
    "capo_opensearch.types.vpc_endpoint_summary.VpcEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointSummaryList) -> list:
    import capo_opensearch.types.vpc_endpoint_summary

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.vpc_endpoint_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> VpcEndpointSummaryList:
    import capo_opensearch.types.vpc_endpoint_summary

    out: VpcEndpointSummaryList = []
    for item in data:
        out.append(capo_opensearch.types.vpc_endpoint_summary.deserialize_json(item))
    return out
