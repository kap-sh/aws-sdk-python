"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetResourcePoliciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.next_token
    import aws_sdk_ssm_incidents.types.resource_policy_list


class GetResourcePoliciesOutput(TypedDict, closed=True):
    resource_policies: (
        "aws_sdk_ssm_incidents.types.resource_policy_list.ResourcePolicyList"
    )
    """<p>Details about the resource policy attached to the response plan.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePoliciesOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.resource_policy_list

    out["resourcePolicies"] = (
        aws_sdk_ssm_incidents.types.resource_policy_list.serialize_json(
            value["resource_policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourcePoliciesOutput:
    out: GetResourcePoliciesOutput = {}  # type: ignore[typeddict-item]
    if "resourcePolicies" in data:
        import aws_sdk_ssm_incidents.types.resource_policy_list

        out["resource_policies"] = (
            aws_sdk_ssm_incidents.types.resource_policy_list.deserialize_json(
                data["resourcePolicies"]
            )
        )
    else:
        raise DeserializationError(
            "GetResourcePoliciesOutput.resource_policies required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
