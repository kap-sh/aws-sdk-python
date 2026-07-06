"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteKnownHostKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DeleteKnownHostKeysRequest(TypedDict, closed=True):
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance for which you want to reset the host key or certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteKnownHostKeysRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteKnownHostKeysRequest:
    out: DeleteKnownHostKeysRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("DeleteKnownHostKeysRequest.instance_name required")
    return out
