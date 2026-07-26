"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#GetDeploymentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.edge_deployments


class GetDeploymentsResult(TypedDict, closed=True):
    deployments: NotRequired[
        "capo_sagemaker_edge.types.edge_deployments.EdgeDeployments"
    ]
    """<p>Returns a list of the configurations of the active deployments on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentsResult) -> dict:
    out: dict = {}
    if "deployments" in value:
        import capo_sagemaker_edge.types.edge_deployments

        out["Deployments"] = capo_sagemaker_edge.types.edge_deployments.serialize_json(
            value["deployments"]
        )
    return out


def deserialize_json(data: dict) -> GetDeploymentsResult:
    out: GetDeploymentsResult = {}  # type: ignore[typeddict-item]
    if "Deployments" in data:
        import capo_sagemaker_edge.types.edge_deployments

        out["deployments"] = (
            capo_sagemaker_edge.types.edge_deployments.deserialize_json(
                data["Deployments"]
            )
        )
    return out
