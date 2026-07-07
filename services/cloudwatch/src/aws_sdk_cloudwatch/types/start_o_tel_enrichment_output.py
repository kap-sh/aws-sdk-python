"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StartOTelEnrichmentOutput``."""

from typing_extensions import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class StartOTelEnrichmentOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartOTelEnrichmentOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StartOTelEnrichmentOutput:
    out: StartOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StartOTelEnrichmentOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StartOTelEnrichmentOutput:
    out: StartOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    return out
