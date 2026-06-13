"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteServiceFunctionResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.resource_list


class DeleteServiceFunctionResourcesResponse(TypedDict):
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    service_function_id: NotRequired["aws_sdk_resiliencehubv2.types.entity_id.EntityId"]
    """<p>The identifier of the service function.</p>"""
    resources: NotRequired["aws_sdk_resiliencehubv2.types.resource_list.ResourceList"]
    """<p>The list of resources that were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceFunctionResourcesResponse) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_function_id" in value:
        out["serviceFunctionId"] = value["service_function_id"]
    if "resources" in value:
        import aws_sdk_resiliencehubv2.types.resource_list

        out["resources"] = aws_sdk_resiliencehubv2.types.resource_list.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> DeleteServiceFunctionResourcesResponse:
    out: DeleteServiceFunctionResourcesResponse = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    if "resources" in data:
        import aws_sdk_resiliencehubv2.types.resource_list

        out["resources"] = aws_sdk_resiliencehubv2.types.resource_list.deserialize_json(
            data["resources"]
        )
    return out
