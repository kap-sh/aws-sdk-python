"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#TunnelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.tunnel_summary

TunnelSummaryList: TypeAlias = list[
    "aws_sdk_iotsecuretunneling.types.tunnel_summary.TunnelSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TunnelSummaryList) -> list:
    import aws_sdk_iotsecuretunneling.types.tunnel_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsecuretunneling.types.tunnel_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TunnelSummaryList:
    import aws_sdk_iotsecuretunneling.types.tunnel_summary

    out: TunnelSummaryList = []
    for item in data:
        out.append(
            aws_sdk_iotsecuretunneling.types.tunnel_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
