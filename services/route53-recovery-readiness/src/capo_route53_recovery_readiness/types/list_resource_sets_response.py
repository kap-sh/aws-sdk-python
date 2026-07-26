"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListResourceSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_resource_set_output
    import capo_route53_recovery_readiness.types.__string


class ListResourceSetsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    resource_sets: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_resource_set_output.__listOfResourceSetOutput"
    ]
    """<p>A list of resource sets associated with the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceSetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "resource_sets" in value:
        import capo_route53_recovery_readiness.types.__list_of_resource_set_output

        out["resourceSets"] = (
            capo_route53_recovery_readiness.types.__list_of_resource_set_output.serialize_json(
                value["resource_sets"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListResourceSetsResponse:
    out: ListResourceSetsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "resourceSets" in data:
        import capo_route53_recovery_readiness.types.__list_of_resource_set_output

        out["resource_sets"] = (
            capo_route53_recovery_readiness.types.__list_of_resource_set_output.deserialize_json(
                data["resourceSets"]
            )
        )
    return out
