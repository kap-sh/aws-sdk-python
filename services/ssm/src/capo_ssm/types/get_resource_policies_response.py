"""Generated from Smithy shape ``com.amazonaws.ssm#GetResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.get_resource_policies_response_entries
    import capo_ssm.types.string


class GetResourcePoliciesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm.types.string.String"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    policies: NotRequired[
        "capo_ssm.types.get_resource_policies_response_entries.GetResourcePoliciesResponseEntries"
    ]
    """<p>An array of the <code>Policy</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "policies" in value:
        import capo_ssm.types.get_resource_policies_response_entries

        out["Policies"] = (
            capo_ssm.types.get_resource_policies_response_entries.serialize_aws_json_1_1(
                value["policies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePoliciesResponse:
    out: GetResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Policies") is not None:
        import capo_ssm.types.get_resource_policies_response_entries

        out["policies"] = (
            capo_ssm.types.get_resource_policies_response_entries.deserialize_aws_json_1_1(
                data["Policies"]
            )
        )
    return out
