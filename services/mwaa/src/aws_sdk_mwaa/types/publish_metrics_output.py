"""Generated from Smithy shape ``com.amazonaws.mwaa#PublishMetricsOutput``."""

from typing_extensions import TypedDict


class PublishMetricsOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PublishMetricsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PublishMetricsOutput:
    out: PublishMetricsOutput = {}  # type: ignore[typeddict-item]
    return out
