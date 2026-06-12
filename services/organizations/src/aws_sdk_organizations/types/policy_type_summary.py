"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.policy_type
    import aws_sdk_organizations.types.policy_type_status


class PolicyTypeSummary(TypedDict):
    type: NotRequired["aws_sdk_organizations.types.policy_type.PolicyType"]
    """<p>The name of the policy type.</p>"""
    status: NotRequired[
        "aws_sdk_organizations.types.policy_type_status.PolicyTypeStatus"
    ]
    """<p>The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypeSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_organizations.types.policy_type

        out["Type"] = aws_sdk_organizations.types.policy_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_organizations.types.policy_type_status

        out["Status"] = (
            aws_sdk_organizations.types.policy_type_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyTypeSummary:
    out: PolicyTypeSummary = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_organizations.types.policy_type

        out["type"] = aws_sdk_organizations.types.policy_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Status" in data:
        import aws_sdk_organizations.types.policy_type_status

        out["status"] = (
            aws_sdk_organizations.types.policy_type_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
