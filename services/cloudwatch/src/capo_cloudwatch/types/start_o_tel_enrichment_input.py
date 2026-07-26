"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StartOTelEnrichmentInput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class StartOTelEnrichmentInput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartOTelEnrichmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StartOTelEnrichmentInput:
    out: StartOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StartOTelEnrichmentInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StartOTelEnrichmentInput:
    out: StartOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    return out
