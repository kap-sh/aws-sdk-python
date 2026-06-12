"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetOTelEnrichmentInput``."""

from typing import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class GetOTelEnrichmentInput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOTelEnrichmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOTelEnrichmentInput:
    out: GetOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOTelEnrichmentInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> GetOTelEnrichmentInput:
    out: GetOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    return out
