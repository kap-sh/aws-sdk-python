"""Generated from Smithy shape ``com.amazonaws.firehose#DirectPutSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.throughput_hint_in_m_bs


class DirectPutSourceConfiguration(TypedDict):
    throughput_hint_in_m_bs: (
        "aws_sdk_firehose.types.throughput_hint_in_m_bs.ThroughputHintInMBs"
    )
    r"""<p> The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit. You can use the <a href=\"https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits\">Firehose Limits form</a> to request a throughput limit increase. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectPutSourceConfiguration) -> dict:
    out: dict = {}
    out["ThroughputHintInMBs"] = value["throughput_hint_in_m_bs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectPutSourceConfiguration:
    out: DirectPutSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "ThroughputHintInMBs" in data:
        out["throughput_hint_in_m_bs"] = data["ThroughputHintInMBs"]
    else:
        raise DeserializationError(
            "DirectPutSourceConfiguration.throughput_hint_in_m_bs required"
        )
    return out
