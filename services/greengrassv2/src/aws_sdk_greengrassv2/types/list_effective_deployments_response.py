"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListEffectiveDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.effective_deployments_list
    import aws_sdk_greengrassv2.types.next_token_string


class ListEffectiveDeploymentsResponse(TypedDict):
    effective_deployments: NotRequired[
        "aws_sdk_greengrassv2.types.effective_deployments_list.EffectiveDeploymentsList"
    ]
    """<p>A list that summarizes each deployment on the core device.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEffectiveDeploymentsResponse) -> dict:
    out: dict = {}
    if "effective_deployments" in value:
        import aws_sdk_greengrassv2.types.effective_deployments_list

        out["effectiveDeployments"] = (
            aws_sdk_greengrassv2.types.effective_deployments_list.serialize_json(
                value["effective_deployments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEffectiveDeploymentsResponse:
    out: ListEffectiveDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "effectiveDeployments" in data:
        import aws_sdk_greengrassv2.types.effective_deployments_list

        out["effective_deployments"] = (
            aws_sdk_greengrassv2.types.effective_deployments_list.deserialize_json(
                data["effectiveDeployments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
