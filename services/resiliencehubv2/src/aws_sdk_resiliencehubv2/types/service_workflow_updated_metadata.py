"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceWorkflowUpdatedMetadata``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ServiceWorkflowUpdatedMetadata(TypedDict):
    service_function_id: NotRequired["str"]
    """<p>The identifier of the service function.</p>"""
    service_function_name: NotRequired["str"]
    """<p>The name of the service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceWorkflowUpdatedMetadata) -> dict:
    out: dict = {}
    if "service_function_id" in value:
        out["serviceFunctionId"] = value["service_function_id"]
    if "service_function_name" in value:
        out["serviceFunctionName"] = value["service_function_name"]
    return out


def deserialize_json(data: dict) -> ServiceWorkflowUpdatedMetadata:
    out: ServiceWorkflowUpdatedMetadata = {}  # type: ignore[typeddict-item]
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    if "serviceFunctionName" in data:
        out["service_function_name"] = data["serviceFunctionName"]
    return out
