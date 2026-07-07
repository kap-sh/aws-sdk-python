"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListSuggestedResiliencyPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.next_token
    import aws_sdk_resiliencehub.types.resiliency_policies


class ListSuggestedResiliencyPoliciesResponse(TypedDict, closed=True):
    resiliency_policies: (
        "aws_sdk_resiliencehub.types.resiliency_policies.ResiliencyPolicies"
    )
    """<p>The suggested resiliency policies for the Resilience Hub applications.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuggestedResiliencyPoliciesResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.resiliency_policies

    out["resiliencyPolicies"] = (
        aws_sdk_resiliencehub.types.resiliency_policies.serialize_json(
            value["resiliency_policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSuggestedResiliencyPoliciesResponse:
    out: ListSuggestedResiliencyPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "resiliencyPolicies" in data:
        import aws_sdk_resiliencehub.types.resiliency_policies

        out["resiliency_policies"] = (
            aws_sdk_resiliencehub.types.resiliency_policies.deserialize_json(
                data["resiliencyPolicies"]
            )
        )
    else:
        raise DeserializationError(
            "ListSuggestedResiliencyPoliciesResponse.resiliency_policies required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
