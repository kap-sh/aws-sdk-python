"""Generated from Smithy shape ``com.amazonaws.wafv2#AssociateWebACLResponse``."""

from typing_extensions import TypedDict


class AssociateWebACLResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateWebACLResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateWebACLResponse:
    out: AssociateWebACLResponse = {}  # type: ignore[typeddict-item]
    return out
