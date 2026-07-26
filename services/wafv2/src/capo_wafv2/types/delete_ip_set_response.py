"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteIPSetResponse``."""

from typing_extensions import TypedDict


class DeleteIPSetResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIPSetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIPSetResponse:
    out: DeleteIPSetResponse = {}  # type: ignore[typeddict-item]
    return out
