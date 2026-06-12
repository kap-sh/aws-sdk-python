"""Generated from Smithy shape ``com.amazonaws.appflow#MarketoConnectorProfileProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.instance_url


class MarketoConnectorProfileProperties(TypedDict):
    instance_url: "aws_sdk_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the Marketo resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketoConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> MarketoConnectorProfileProperties:
    out: MarketoConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "MarketoConnectorProfileProperties.instance_url required"
        )
    return out
