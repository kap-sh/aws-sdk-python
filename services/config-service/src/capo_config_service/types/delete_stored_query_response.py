"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteStoredQueryResponse``."""

from typing_extensions import TypedDict


class DeleteStoredQueryResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStoredQueryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStoredQueryResponse:
    out: DeleteStoredQueryResponse = {}  # type: ignore[typeddict-item]
    return out
