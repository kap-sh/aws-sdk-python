"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.resource_name


class GetServiceSyncConfigInput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want to get the service sync configuration for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceSyncConfigInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceSyncConfigInput:
    out: GetServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("GetServiceSyncConfigInput.service_name required")
    return out
