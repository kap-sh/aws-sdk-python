"""Generated from Smithy shape ``com.amazonaws.amp#RuleGroupsNamespaceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.rule_groups_namespace_status_code


class RuleGroupsNamespaceStatus(TypedDict, closed=True):
    status_code: "aws_sdk_amp.types.rule_groups_namespace_status_code.RuleGroupsNamespaceStatusCode"
    """<p>The current status of the namespace.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the failure, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupsNamespaceStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> RuleGroupsNamespaceStatus:
    out: RuleGroupsNamespaceStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError("RuleGroupsNamespaceStatus.status_code required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
