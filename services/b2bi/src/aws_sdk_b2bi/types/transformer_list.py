"""Generated from Smithy shape ``com.amazonaws.b2bi#TransformerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.transformer_summary

TransformerList: TypeAlias = list[
    "aws_sdk_b2bi.types.transformer_summary.TransformerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformerList) -> list:
    import aws_sdk_b2bi.types.transformer_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_b2bi.types.transformer_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TransformerList:
    import aws_sdk_b2bi.types.transformer_summary

    out: TransformerList = []
    for item in data:
        out.append(
            aws_sdk_b2bi.types.transformer_summary.deserialize_aws_json_1_0(item)
        )
    return out
