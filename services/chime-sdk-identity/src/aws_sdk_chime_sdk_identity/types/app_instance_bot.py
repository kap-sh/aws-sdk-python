"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceBot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.configuration
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.resource_name
    import aws_sdk_chime_sdk_identity.types.timestamp


class AppInstanceBot(TypedDict):
    app_instance_bot_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the AppInstanceBot.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The name of the AppInstanceBot.</p>"""
    configuration: NotRequired[
        "aws_sdk_chime_sdk_identity.types.configuration.Configuration"
    ]
    """<p>The data processing instructions for an AppInstanceBot.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which the <code>AppInstanceBot</code> was created.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which the <code>AppInstanceBot</code> was last updated.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata for an AppInstanceBot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceBot) -> dict:
    out: dict = {}
    if "app_instance_bot_arn" in value:
        out["AppInstanceBotArn"] = value["app_instance_bot_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import aws_sdk_chime_sdk_identity.types.configuration

        out["Configuration"] = (
            aws_sdk_chime_sdk_identity.types.configuration.serialize_json(
                value["configuration"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstanceBot:
    out: AppInstanceBot = {}  # type: ignore[typeddict-item]
    if "AppInstanceBotArn" in data:
        out["app_instance_bot_arn"] = data["AppInstanceBotArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Configuration" in data:
        import aws_sdk_chime_sdk_identity.types.configuration

        out["configuration"] = (
            aws_sdk_chime_sdk_identity.types.configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    return out
