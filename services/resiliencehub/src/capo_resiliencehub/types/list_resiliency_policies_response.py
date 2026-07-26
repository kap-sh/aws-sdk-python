"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListResiliencyPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.resiliency_policies


class ListResiliencyPoliciesResponse(TypedDict, closed=True):
    resiliency_policies: (
        "capo_resiliencehub.types.resiliency_policies.ResiliencyPolicies"
    )
    """<p>The resiliency policies for the Resilience Hub applications.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResiliencyPoliciesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.resiliency_policies

    out["resiliencyPolicies"] = (
        capo_resiliencehub.types.resiliency_policies.serialize_json(
            value["resiliency_policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResiliencyPoliciesResponse:
    out: ListResiliencyPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "resiliencyPolicies" in data:
        import capo_resiliencehub.types.resiliency_policies

        out["resiliency_policies"] = (
            capo_resiliencehub.types.resiliency_policies.deserialize_json(
                data["resiliencyPolicies"]
            )
        )
    else:
        raise DeserializationError(
            "ListResiliencyPoliciesResponse.resiliency_policies required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
