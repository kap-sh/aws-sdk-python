"""Generated from Smithy shape ``com.amazonaws.appflow#SlackConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.instance_url


class SlackConnectorProfileProperties(TypedDict, closed=True):
    instance_url: "capo_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the Slack resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> SlackConnectorProfileProperties:
    out: SlackConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "SlackConnectorProfileProperties.instance_url required"
        )
    return out
