"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteAPIKeyResponse``."""

from typing_extensions import TypedDict


class DeleteAPIKeyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAPIKeyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAPIKeyResponse:
    out: DeleteAPIKeyResponse = {}  # type: ignore[typeddict-item]
    return out
