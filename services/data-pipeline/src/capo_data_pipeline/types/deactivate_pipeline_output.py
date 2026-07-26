"""Generated from Smithy shape ``com.amazonaws.datapipeline#DeactivatePipelineOutput``."""

from typing_extensions import TypedDict


class DeactivatePipelineOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeactivatePipelineOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeactivatePipelineOutput:
    out: DeactivatePipelineOutput = {}  # type: ignore[typeddict-item]
    return out
