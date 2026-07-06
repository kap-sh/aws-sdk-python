"""Generated from Smithy shape ``com.amazonaws.appflow#DynatraceConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.instance_url


class DynatraceConnectorProfileProperties(TypedDict, closed=True):
    instance_url: "aws_sdk_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the Dynatrace resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> DynatraceConnectorProfileProperties:
    out: DynatraceConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "DynatraceConnectorProfileProperties.instance_url required"
        )
    return out
