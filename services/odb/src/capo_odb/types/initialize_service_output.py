"""Generated from Smithy shape ``com.amazonaws.odb#InitializeServiceOutput``."""

from typing_extensions import TypedDict


class InitializeServiceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InitializeServiceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> InitializeServiceOutput:
    out: InitializeServiceOutput = {}  # type: ignore[typeddict-item]
    return out
