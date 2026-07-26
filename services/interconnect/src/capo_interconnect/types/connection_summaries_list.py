"""Generated from Smithy shape ``com.amazonaws.interconnect#ConnectionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_interconnect.types.connection_summary

ConnectionSummariesList: TypeAlias = list[
    "capo_interconnect.types.connection_summary.ConnectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionSummariesList) -> list:
    import capo_interconnect.types.connection_summary

    out: list = []
    for item in value:
        out.append(
            capo_interconnect.types.connection_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectionSummariesList:
    import capo_interconnect.types.connection_summary

    out: ConnectionSummariesList = []
    for item in data:
        out.append(
            capo_interconnect.types.connection_summary.deserialize_aws_json_1_0(item)
        )
    return out
