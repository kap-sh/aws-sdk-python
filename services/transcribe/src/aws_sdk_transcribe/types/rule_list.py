"""Generated from Smithy shape ``com.amazonaws.transcribe#RuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.rule

RuleList: TypeAlias = list["aws_sdk_transcribe.types.rule.Rule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleList) -> list:
    import aws_sdk_transcribe.types.rule

    out: list = []
    for item in value:
        out.append(aws_sdk_transcribe.types.rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleList:
    import aws_sdk_transcribe.types.rule

    out: RuleList = []
    for item in data:
        out.append(aws_sdk_transcribe.types.rule.deserialize_aws_json_1_1(item))
    return out
