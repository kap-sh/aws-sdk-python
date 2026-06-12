"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudsterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.fraudster_summary

FraudsterSummaries: TypeAlias = list[
    "aws_sdk_voice_id.types.fraudster_summary.FraudsterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudsterSummaries) -> list:
    import aws_sdk_voice_id.types.fraudster_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_voice_id.types.fraudster_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FraudsterSummaries:
    import aws_sdk_voice_id.types.fraudster_summary

    out: FraudsterSummaries = []
    for item in data:
        out.append(
            aws_sdk_voice_id.types.fraudster_summary.deserialize_aws_json_1_0(item)
        )
    return out
