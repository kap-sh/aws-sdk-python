"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.instance_url


class InforNexusConnectorProfileProperties(TypedDict, closed=True):
    instance_url: "capo_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the Infor Nexus resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InforNexusConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> InforNexusConnectorProfileProperties:
    out: InforNexusConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "InforNexusConnectorProfileProperties.instance_url required"
        )
    return out
