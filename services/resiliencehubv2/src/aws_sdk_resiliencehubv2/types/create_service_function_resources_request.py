"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateServiceFunctionResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.resource_list


class CreateServiceFunctionResourcesRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId"
    """<p>The identifier of the service function to associate resources with.</p>"""
    resources: "aws_sdk_resiliencehubv2.types.resource_list.ResourceList"
    """<p>The list of resources to associate with the service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceFunctionResourcesRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    import aws_sdk_resiliencehubv2.types.resource_list

    out["resources"] = aws_sdk_resiliencehubv2.types.resource_list.serialize_json(
        value["resources"]
    )
    return out


def deserialize_json(data: dict) -> CreateServiceFunctionResourcesRequest:
    out: CreateServiceFunctionResourcesRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "CreateServiceFunctionResourcesRequest.service_arn required"
        )
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        raise DeserializationError(
            "CreateServiceFunctionResourcesRequest.service_function_id required"
        )
    if "resources" in data:
        import aws_sdk_resiliencehubv2.types.resource_list

        out["resources"] = aws_sdk_resiliencehubv2.types.resource_list.deserialize_json(
            data["resources"]
        )
    else:
        raise DeserializationError(
            "CreateServiceFunctionResourcesRequest.resources required"
        )
    return out
