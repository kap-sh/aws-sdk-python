"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteAccessControlRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_name
    import capo_workmail.types.organization_id


class DeleteAccessControlRuleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization.</p>"""
    name: "capo_workmail.types.access_control_rule_name.AccessControlRuleName"
    """<p>The name of the access control rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccessControlRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccessControlRuleRequest:
    out: DeleteAccessControlRuleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteAccessControlRuleRequest.organization_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteAccessControlRuleRequest.name required")
    return out
