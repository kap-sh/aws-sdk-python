"""Generated from Smithy shape ``com.amazonaws.fms#PolicyComplianceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.compliance_violators
    import aws_sdk_fms.types.issue_info_map
    import aws_sdk_fms.types.policy_id
    import aws_sdk_fms.types.time_stamp


class PolicyComplianceDetail(TypedDict, closed=True):
    policy_owner: NotRequired["aws_sdk_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account that created the Firewall Manager policy.</p>"""
    policy_id: NotRequired["aws_sdk_fms.types.policy_id.PolicyId"]
    """<p>The ID of the Firewall Manager policy.</p>"""
    member_account: NotRequired["aws_sdk_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    violators: NotRequired["aws_sdk_fms.types.compliance_violators.ComplianceViolators"]
    """<p>An array of resources that aren't protected by the WAF or Shield Advanced policy or that aren't in compliance with the security group policy.</p>"""
    evaluation_limit_exceeded: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Indicates if over 100 resources are noncompliant with the Firewall Manager policy.</p>"""
    expired_at: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>A timestamp that indicates when the returned information should be considered out of date.</p>"""
    issue_info_map: NotRequired["aws_sdk_fms.types.issue_info_map.IssueInfoMap"]
    """<p>Details about problems with dependent services, such as WAF or Config, and the error message received that indicates the problem with the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyComplianceDetail) -> dict:
    out: dict = {}
    if "policy_owner" in value:
        out["PolicyOwner"] = value["policy_owner"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "member_account" in value:
        out["MemberAccount"] = value["member_account"]
    if "violators" in value:
        import aws_sdk_fms.types.compliance_violators

        out["Violators"] = (
            aws_sdk_fms.types.compliance_violators.serialize_aws_json_1_1(
                value["violators"]
            )
        )
    out["EvaluationLimitExceeded"] = value.get("evaluation_limit_exceeded", False)
    if "expired_at" in value:
        import aws_sdk_fms.types.time_stamp

        out["ExpiredAt"] = aws_sdk_fms.types.time_stamp.serialize_aws_json_1_1(
            value["expired_at"]
        )
    if "issue_info_map" in value:
        import aws_sdk_fms.types.issue_info_map

        out["IssueInfoMap"] = aws_sdk_fms.types.issue_info_map.serialize_aws_json_1_1(
            value["issue_info_map"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyComplianceDetail:
    out: PolicyComplianceDetail = {}  # type: ignore[typeddict-item]
    if "PolicyOwner" in data:
        out["policy_owner"] = data["PolicyOwner"]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "MemberAccount" in data:
        out["member_account"] = data["MemberAccount"]
    if "Violators" in data:
        import aws_sdk_fms.types.compliance_violators

        out["violators"] = (
            aws_sdk_fms.types.compliance_violators.deserialize_aws_json_1_1(
                data["Violators"]
            )
        )
    if "EvaluationLimitExceeded" in data:
        out["evaluation_limit_exceeded"] = data["EvaluationLimitExceeded"]
    else:
        out["evaluation_limit_exceeded"] = False
    if "ExpiredAt" in data:
        import aws_sdk_fms.types.time_stamp

        out["expired_at"] = aws_sdk_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["ExpiredAt"]
        )
    if "IssueInfoMap" in data:
        import aws_sdk_fms.types.issue_info_map

        out["issue_info_map"] = (
            aws_sdk_fms.types.issue_info_map.deserialize_aws_json_1_1(
                data["IssueInfoMap"]
            )
        )
    return out
