"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.resource_policy


class DescribeResourcePolicyResponse(TypedDict):
    resource_policy: NotRequired[
        "aws_sdk_organizations.types.resource_policy.ResourcePolicy"
    ]
    """<p>A structure that contains details about the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        import aws_sdk_organizations.types.resource_policy

        out["ResourcePolicy"] = (
            aws_sdk_organizations.types.resource_policy.serialize_aws_json_1_1(
                value["resource_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResourcePolicy" in data:
        import aws_sdk_organizations.types.resource_policy

        out["resource_policy"] = (
            aws_sdk_organizations.types.resource_policy.deserialize_aws_json_1_1(
                data["ResourcePolicy"]
            )
        )
    return out
