"""Generated from Smithy shape ``com.amazonaws.mediastore#DeleteContainerOutput``."""

from typing_extensions import TypedDict


class DeleteContainerOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContainerOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContainerOutput:
    out: DeleteContainerOutput = {}  # type: ignore[typeddict-item]
    return out
