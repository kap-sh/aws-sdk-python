"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteWebACLResponse``."""

from typing_extensions import TypedDict


class DeleteWebACLResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebACLResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebACLResponse:
    out: DeleteWebACLResponse = {}  # type: ignore[typeddict-item]
    return out
