"""Generated from Smithy shape ``com.amazonaws.appflow#ServiceNowConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.instance_url


class ServiceNowConnectorProfileProperties(TypedDict, closed=True):
    instance_url: "capo_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the ServiceNow resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> ServiceNowConnectorProfileProperties:
    out: ServiceNowConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "ServiceNowConnectorProfileProperties.instance_url required"
        )
    return out
