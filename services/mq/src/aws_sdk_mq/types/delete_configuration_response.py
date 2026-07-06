"""Generated from Smithy shape ``com.amazonaws.mq#DeleteConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class DeleteConfigurationResponse(TypedDict, closed=True):
    configuration_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    return out


def deserialize_json(data: dict) -> DeleteConfigurationResponse:
    out: DeleteConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    return out
