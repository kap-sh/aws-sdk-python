"""Generated from Smithy shape ``com.amazonaws.devopsguru#StartCostEstimationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.client_token
    import capo_devops_guru.types.cost_estimation_resource_collection_filter


class StartCostEstimationRequest(TypedDict, closed=True):
    resource_collection: "capo_devops_guru.types.cost_estimation_resource_collection_filter.CostEstimationResourceCollectionFilter"
    """<p>The collection of Amazon Web Services resources used to create a monthly DevOps Guru cost estimate.</p>"""
    client_token: NotRequired["capo_devops_guru.types.client_token.ClientToken"]
    """<p>The idempotency token used to identify each cost estimate request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCostEstimationRequest) -> dict:
    out: dict = {}
    import capo_devops_guru.types.cost_estimation_resource_collection_filter

    out["ResourceCollection"] = (
        capo_devops_guru.types.cost_estimation_resource_collection_filter.serialize_json(
            value["resource_collection"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartCostEstimationRequest:
    out: StartCostEstimationRequest = {}  # type: ignore[typeddict-item]
    if "ResourceCollection" in data:
        import capo_devops_guru.types.cost_estimation_resource_collection_filter

        out["resource_collection"] = (
            capo_devops_guru.types.cost_estimation_resource_collection_filter.deserialize_json(
                data["ResourceCollection"]
            )
        )
    else:
        raise DeserializationError(
            "StartCostEstimationRequest.resource_collection required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
