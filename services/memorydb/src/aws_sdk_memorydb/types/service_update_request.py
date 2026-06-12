"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class ServiceUpdateRequest(TypedDict):
    service_update_name_to_apply: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The unique ID of the service update</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateRequest) -> dict:
    out: dict = {}
    if "service_update_name_to_apply" in value:
        out["ServiceUpdateNameToApply"] = value["service_update_name_to_apply"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceUpdateRequest:
    out: ServiceUpdateRequest = {}  # type: ignore[typeddict-item]
    if "ServiceUpdateNameToApply" in data:
        out["service_update_name_to_apply"] = data["ServiceUpdateNameToApply"]
    return out
