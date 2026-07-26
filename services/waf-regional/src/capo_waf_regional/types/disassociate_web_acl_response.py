"""Generated from Smithy shape ``com.amazonaws.wafregional#DisassociateWebACLResponse``."""

from typing_extensions import TypedDict


class DisassociateWebACLResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateWebACLResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateWebACLResponse:
    out: DisassociateWebACLResponse = {}  # type: ignore[typeddict-item]
    return out
