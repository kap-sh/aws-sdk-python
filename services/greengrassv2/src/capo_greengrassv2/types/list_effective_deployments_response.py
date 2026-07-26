"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListEffectiveDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.effective_deployments_list
    import capo_greengrassv2.types.next_token_string


class ListEffectiveDeploymentsResponse(TypedDict, closed=True):
    effective_deployments: NotRequired[
        "capo_greengrassv2.types.effective_deployments_list.EffectiveDeploymentsList"
    ]
    """<p>A list that summarizes each deployment on the core device.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEffectiveDeploymentsResponse) -> dict:
    out: dict = {}
    if "effective_deployments" in value:
        import capo_greengrassv2.types.effective_deployments_list

        out["effectiveDeployments"] = (
            capo_greengrassv2.types.effective_deployments_list.serialize_json(
                value["effective_deployments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEffectiveDeploymentsResponse:
    out: ListEffectiveDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "effectiveDeployments" in data:
        import capo_greengrassv2.types.effective_deployments_list

        out["effective_deployments"] = (
            capo_greengrassv2.types.effective_deployments_list.deserialize_json(
                data["effectiveDeployments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
