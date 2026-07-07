"""Generated from Smithy shape ``com.amazonaws.shield#AssociateDRTRoleResponse``."""

from typing_extensions import TypedDict


class AssociateDRTRoleResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateDRTRoleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateDRTRoleResponse:
    out: AssociateDRTRoleResponse = {}  # type: ignore[typeddict-item]
    return out
