"""Generated from Smithy shape ``com.amazonaws.organizations#ListPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.next_token
    import aws_sdk_organizations.types.policies


class ListPoliciesResponse(TypedDict, closed=True):
    policies: NotRequired["aws_sdk_organizations.types.policies.Policies"]
    """<p>A list of policies that match the filter criteria in the request. The output list doesn't include the policy contents. To see the content for a policy, see <a>DescribePolicy</a>.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_organizations.types.policies

        out["Policies"] = aws_sdk_organizations.types.policies.serialize_aws_json_1_1(
            value["policies"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "Policies" in data:
        import aws_sdk_organizations.types.policies

        out["policies"] = aws_sdk_organizations.types.policies.deserialize_aws_json_1_1(
            data["Policies"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
