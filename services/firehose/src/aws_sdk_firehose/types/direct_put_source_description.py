"""Generated from Smithy shape ``com.amazonaws.firehose#DirectPutSourceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.throughput_hint_in_m_bs


class DirectPutSourceDescription(TypedDict):
    throughput_hint_in_m_bs: NotRequired[
        "aws_sdk_firehose.types.throughput_hint_in_m_bs.ThroughputHintInMBs"
    ]
    """<p> The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit. You can use the <a href=\"https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits\">Firehose Limits form</a> to request a throughput limit increase. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectPutSourceDescription) -> dict:
    out: dict = {}
    if "throughput_hint_in_m_bs" in value:
        out["ThroughputHintInMBs"] = value["throughput_hint_in_m_bs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectPutSourceDescription:
    out: DirectPutSourceDescription = {}  # type: ignore[typeddict-item]
    if "ThroughputHintInMBs" in data:
        out["throughput_hint_in_m_bs"] = data["ThroughputHintInMBs"]
    return out
