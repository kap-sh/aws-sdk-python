"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutAnomalyDetectorOutput``."""

from typing_extensions import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class PutAnomalyDetectorOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAnomalyDetectorOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAnomalyDetectorOutput:
    out: PutAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAnomalyDetectorOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutAnomalyDetectorOutput:
    out: PutAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out
