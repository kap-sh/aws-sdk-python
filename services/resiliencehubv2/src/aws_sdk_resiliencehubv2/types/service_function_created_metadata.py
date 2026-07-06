"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionCreatedMetadata``."""

from typing_extensions import NotRequired, TypedDict


class ServiceFunctionCreatedMetadata(TypedDict, closed=True):
    service_function_id: NotRequired["str"]
    """<p>The identifier of the created service function.</p>"""
    service_function_name: NotRequired["str"]
    """<p>The name of the created service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunctionCreatedMetadata) -> dict:
    out: dict = {}
    if "service_function_id" in value:
        out["serviceFunctionId"] = value["service_function_id"]
    if "service_function_name" in value:
        out["serviceFunctionName"] = value["service_function_name"]
    return out


def deserialize_json(data: dict) -> ServiceFunctionCreatedMetadata:
    out: ServiceFunctionCreatedMetadata = {}  # type: ignore[typeddict-item]
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    if "serviceFunctionName" in data:
        out["service_function_name"] = data["serviceFunctionName"]
    return out
