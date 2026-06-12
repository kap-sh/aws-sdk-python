"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutInsightRuleOutput``."""

from typing import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class PutInsightRuleOutput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutInsightRuleOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> PutInsightRuleOutput:
    out: PutInsightRuleOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutInsightRuleOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutInsightRuleOutput:
    out: PutInsightRuleOutput = {}  # type: ignore[typeddict-item]
    return out
