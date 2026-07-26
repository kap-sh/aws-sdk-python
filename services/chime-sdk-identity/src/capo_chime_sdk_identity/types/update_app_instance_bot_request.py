"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.configuration
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.resource_name


class UpdateAppInstanceBotRequest(TypedDict, closed=True):
    app_instance_bot_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceBot</code>.</p>"""
    name: "capo_chime_sdk_identity.types.resource_name.ResourceName"
    """<p>The name of the <code>AppInstanceBot</code>.</p>"""
    metadata: "capo_chime_sdk_identity.types.metadata.Metadata"
    """<p>The metadata of the <code>AppInstanceBot</code>.</p>"""
    configuration: NotRequired[
        "capo_chime_sdk_identity.types.configuration.Configuration"
    ]
    """<p>The configuration for the bot update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceBotRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Metadata"] = value["metadata"]
    if "configuration" in value:
        import capo_chime_sdk_identity.types.configuration

        out["Configuration"] = (
            capo_chime_sdk_identity.types.configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceBotRequest:
    out: UpdateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateAppInstanceBotRequest.name required")
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    else:
        raise DeserializationError("UpdateAppInstanceBotRequest.metadata required")
    if "Configuration" in data:
        import capo_chime_sdk_identity.types.configuration

        out["configuration"] = (
            capo_chime_sdk_identity.types.configuration.deserialize_json(
                data["Configuration"]
            )
        )
    return out
