"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StopOTelEnrichmentInput``."""

from typing import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class StopOTelEnrichmentInput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopOTelEnrichmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StopOTelEnrichmentInput:
    out: StopOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StopOTelEnrichmentInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StopOTelEnrichmentInput:
    out: StopOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    return out
