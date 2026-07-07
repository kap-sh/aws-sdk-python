"""Generated from Smithy shape ``com.amazonaws.workmail#AssociateMemberToGroupResponse``."""

from typing_extensions import TypedDict


class AssociateMemberToGroupResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateMemberToGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateMemberToGroupResponse:
    out: AssociateMemberToGroupResponse = {}  # type: ignore[typeddict-item]
    return out
