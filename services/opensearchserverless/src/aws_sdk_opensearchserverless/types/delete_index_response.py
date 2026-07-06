"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteIndexResponse``."""

from typing_extensions import TypedDict


class DeleteIndexResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteIndexResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteIndexResponse:
    out: DeleteIndexResponse = {}  # type: ignore[typeddict-item]
    return out
