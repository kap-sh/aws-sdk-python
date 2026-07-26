"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionUpdatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn_list


class ServiceFunctionUpdatedMetadata(TypedDict, closed=True):
    service_function_id: NotRequired["str"]
    """<p>The identifier of the service function.</p>"""
    service_function_name: NotRequired["str"]
    """<p>The name of the service function.</p>"""
    resources_added: NotRequired["capo_resiliencehubv2.types.arn_list.ArnList"]
    """<p>The list of resource ARNs that were added.</p>"""
    resources_removed: NotRequired["capo_resiliencehubv2.types.arn_list.ArnList"]
    """<p>The list of resource ARNs that were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunctionUpdatedMetadata) -> dict:
    out: dict = {}
    if "service_function_id" in value:
        out["serviceFunctionId"] = value["service_function_id"]
    if "service_function_name" in value:
        out["serviceFunctionName"] = value["service_function_name"]
    if "resources_added" in value:
        import capo_resiliencehubv2.types.arn_list

        out["resourcesAdded"] = capo_resiliencehubv2.types.arn_list.serialize_json(
            value["resources_added"]
        )
    if "resources_removed" in value:
        import capo_resiliencehubv2.types.arn_list

        out["resourcesRemoved"] = capo_resiliencehubv2.types.arn_list.serialize_json(
            value["resources_removed"]
        )
    return out


def deserialize_json(data: dict) -> ServiceFunctionUpdatedMetadata:
    out: ServiceFunctionUpdatedMetadata = {}  # type: ignore[typeddict-item]
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    if "serviceFunctionName" in data:
        out["service_function_name"] = data["serviceFunctionName"]
    if "resourcesAdded" in data:
        import capo_resiliencehubv2.types.arn_list

        out["resources_added"] = capo_resiliencehubv2.types.arn_list.deserialize_json(
            data["resourcesAdded"]
        )
    if "resourcesRemoved" in data:
        import capo_resiliencehubv2.types.arn_list

        out["resources_removed"] = capo_resiliencehubv2.types.arn_list.deserialize_json(
            data["resourcesRemoved"]
        )
    return out
