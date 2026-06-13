"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.service_resource_list


class ListResourcesResponse(TypedDict):
    service_function_id: NotRequired["aws_sdk_resiliencehubv2.types.entity_id.EntityId"]
    """<p>The service function identifier for the returned resources.</p>"""
    service_resources: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_resource_list.ServiceResourceList"
    ]
    """<p>The list of service resources.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesResponse) -> dict:
    out: dict = {}
    if "service_function_id" in value:
        out["serviceFunctionId"] = value["service_function_id"]
    if "service_resources" in value:
        import aws_sdk_resiliencehubv2.types.service_resource_list

        out["serviceResources"] = (
            aws_sdk_resiliencehubv2.types.service_resource_list.serialize_json(
                value["service_resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesResponse:
    out: ListResourcesResponse = {}  # type: ignore[typeddict-item]
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    if "serviceResources" in data:
        import aws_sdk_resiliencehubv2.types.service_resource_list

        out["service_resources"] = (
            aws_sdk_resiliencehubv2.types.service_resource_list.deserialize_json(
                data["serviceResources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
