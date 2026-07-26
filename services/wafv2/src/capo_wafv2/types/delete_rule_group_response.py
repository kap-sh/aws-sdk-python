"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteRuleGroupResponse``."""

from typing_extensions import TypedDict


class DeleteRuleGroupResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRuleGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRuleGroupResponse:
    out: DeleteRuleGroupResponse = {}  # type: ignore[typeddict-item]
    return out
