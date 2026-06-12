"""Generated from Smithy shape ``com.amazonaws.cloudwatch#UntagResourceOutput``."""

from typing import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class UntagResourceOutput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagResourceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out
