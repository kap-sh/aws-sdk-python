"""Generated from Smithy shape ``com.amazonaws.ssm#GetResourcePoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.get_resource_policies_response_entries
    import aws_sdk_ssm.types.string


class GetResourcePoliciesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    policies: NotRequired[
        "aws_sdk_ssm.types.get_resource_policies_response_entries.GetResourcePoliciesResponseEntries"
    ]
    """<p>An array of the <code>Policy</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "policies" in value:
        import aws_sdk_ssm.types.get_resource_policies_response_entries

        out["Policies"] = (
            aws_sdk_ssm.types.get_resource_policies_response_entries.serialize_aws_json_1_1(
                value["policies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePoliciesResponse:
    out: GetResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Policies" in data:
        import aws_sdk_ssm.types.get_resource_policies_response_entries

        out["policies"] = (
            aws_sdk_ssm.types.get_resource_policies_response_entries.deserialize_aws_json_1_1(
                data["Policies"]
            )
        )
    return out
