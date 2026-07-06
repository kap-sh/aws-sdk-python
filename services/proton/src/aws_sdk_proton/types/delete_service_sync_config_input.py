"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class DeleteServiceSyncConfigInput(TypedDict, closed=True):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want to delete the service sync configuration for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceSyncConfigInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceSyncConfigInput:
    out: DeleteServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("DeleteServiceSyncConfigInput.service_name required")
    return out
