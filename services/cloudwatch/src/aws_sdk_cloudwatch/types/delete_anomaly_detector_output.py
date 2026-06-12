"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAnomalyDetectorOutput``."""

from typing import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class DeleteAnomalyDetectorOutput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAnomalyDetectorOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAnomalyDetectorOutput:
    out: DeleteAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAnomalyDetectorOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteAnomalyDetectorOutput:
    out: DeleteAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out
