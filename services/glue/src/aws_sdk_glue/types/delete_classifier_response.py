"""Generated from Smithy shape ``com.amazonaws.glue#DeleteClassifierResponse``."""

from typing_extensions import TypedDict


class DeleteClassifierResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClassifierResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClassifierResponse:
    out: DeleteClassifierResponse = {}  # type: ignore[typeddict-item]
    return out
