"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteServiceFunctionResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_id
    import capo_resiliencehubv2.types.resource_list


class DeleteServiceFunctionResourcesRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId"
    """<p>The identifier of the service function to remove resources from.</p>"""
    resources: "capo_resiliencehubv2.types.resource_list.ResourceList"
    """<p>The list of resources to remove from the service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceFunctionResourcesRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    import capo_resiliencehubv2.types.resource_list

    out["resources"] = capo_resiliencehubv2.types.resource_list.serialize_json(
        value["resources"]
    )
    return out


def deserialize_json(data: dict) -> DeleteServiceFunctionResourcesRequest:
    out: DeleteServiceFunctionResourcesRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "DeleteServiceFunctionResourcesRequest.service_arn required"
        )
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        raise DeserializationError(
            "DeleteServiceFunctionResourcesRequest.service_function_id required"
        )
    if "resources" in data:
        import capo_resiliencehubv2.types.resource_list

        out["resources"] = capo_resiliencehubv2.types.resource_list.deserialize_json(
            data["resources"]
        )
    else:
        raise DeserializationError(
            "DeleteServiceFunctionResourcesRequest.resources required"
        )
    return out
