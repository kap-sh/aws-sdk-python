"""Generated from Smithy shape ``com.amazonaws.glue#GetResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.get_resource_policies_response_list
    import capo_glue.types.token


class GetResourcePoliciesResponse(TypedDict, closed=True):
    get_resource_policies_response_list: NotRequired[
        "capo_glue.types.get_resource_policies_response_list.GetResourcePoliciesResponseList"
    ]
    """<p>A list of the individual resource policies and the account-level resource policy.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if the returned list does not contain the last resource policy available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "get_resource_policies_response_list" in value:
        import capo_glue.types.get_resource_policies_response_list

        out["GetResourcePoliciesResponseList"] = (
            capo_glue.types.get_resource_policies_response_list.serialize_aws_json_1_1(
                value["get_resource_policies_response_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePoliciesResponse:
    out: GetResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "GetResourcePoliciesResponseList" in data:
        import capo_glue.types.get_resource_policies_response_list

        out["get_resource_policies_response_list"] = (
            capo_glue.types.get_resource_policies_response_list.deserialize_aws_json_1_1(
                data["GetResourcePoliciesResponseList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
