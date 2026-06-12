"""Generated from Smithy shape ``com.amazonaws.kafka#CreateConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.configuration_revision
    import aws_sdk_kafka.types.configuration_state


class CreateConfigurationResponse(TypedDict):
    arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the configuration was created.</p>"""
    latest_revision: NotRequired[
        "aws_sdk_kafka.types.configuration_revision.ConfigurationRevision"
    ]
    """<p>Latest revision of the configuration.</p>"""
    name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the configuration.</p>"""
    state: NotRequired["aws_sdk_kafka.types.configuration_state.ConfigurationState"]
    """<p>The state of the configuration. The possible states are ACTIVE, DELETING, and DELETE_FAILED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "latest_revision" in value:
        import aws_sdk_kafka.types.configuration_revision

        out["latestRevision"] = (
            aws_sdk_kafka.types.configuration_revision.serialize_json(
                value["latest_revision"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "state" in value:
        import aws_sdk_kafka.types.configuration_state

        out["state"] = aws_sdk_kafka.types.configuration_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> CreateConfigurationResponse:
    out: CreateConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "latestRevision" in data:
        import aws_sdk_kafka.types.configuration_revision

        out["latest_revision"] = (
            aws_sdk_kafka.types.configuration_revision.deserialize_json(
                data["latestRevision"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        import aws_sdk_kafka.types.configuration_state

        out["state"] = aws_sdk_kafka.types.configuration_state.deserialize_json(
            data["state"]
        )
    return out
