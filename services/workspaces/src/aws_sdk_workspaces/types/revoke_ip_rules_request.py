"""Generated from Smithy shape ``com.amazonaws.workspaces#RevokeIpRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_group_id
    import aws_sdk_workspaces.types.ip_revoked_rule_list


class RevokeIpRulesRequest(TypedDict, closed=True):
    group_id: "aws_sdk_workspaces.types.ip_group_id.IpGroupId"
    """<p>The identifier of the group.</p>"""
    user_rules: "aws_sdk_workspaces.types.ip_revoked_rule_list.IpRevokedRuleList"
    """<p>The rules to remove from the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeIpRulesRequest) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    import aws_sdk_workspaces.types.ip_revoked_rule_list

    out["UserRules"] = (
        aws_sdk_workspaces.types.ip_revoked_rule_list.serialize_aws_json_1_1(
            value["user_rules"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeIpRulesRequest:
    out: RevokeIpRulesRequest = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("RevokeIpRulesRequest.group_id required")
    if "UserRules" in data:
        import aws_sdk_workspaces.types.ip_revoked_rule_list

        out["user_rules"] = (
            aws_sdk_workspaces.types.ip_revoked_rule_list.deserialize_aws_json_1_1(
                data["UserRules"]
            )
        )
    else:
        raise DeserializationError("RevokeIpRulesRequest.user_rules required")
    return out
