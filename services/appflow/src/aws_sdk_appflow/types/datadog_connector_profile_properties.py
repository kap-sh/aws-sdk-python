"""Generated from Smithy shape ``com.amazonaws.appflow#DatadogConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.instance_url


class DatadogConnectorProfileProperties(TypedDict, closed=True):
    instance_url: "aws_sdk_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the Datadog resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatadogConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> DatadogConnectorProfileProperties:
    out: DatadogConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "DatadogConnectorProfileProperties.instance_url required"
        )
    return out
