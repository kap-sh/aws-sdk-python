"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateEventBusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.dead_letter_config
    import aws_sdk_eventbridge.types.event_bus_description
    import aws_sdk_eventbridge.types.event_bus_name
    import aws_sdk_eventbridge.types.kms_key_identifier
    import aws_sdk_eventbridge.types.log_config
    import aws_sdk_eventbridge.types.string


class UpdateEventBusResponse(TypedDict):
    arn: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The event bus Amazon Resource Name (ARN).</p>"""
    name: NotRequired["aws_sdk_eventbridge.types.event_bus_name.EventBusName"]
    """<p>The event bus name.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt events on this event bus, if one has been specified.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html\">Data encryption in EventBridge</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_eventbridge.types.dead_letter_config.DeadLetterConfig"
    ]
    log_config: NotRequired["aws_sdk_eventbridge.types.log_config.LogConfig"]
    """<p>The logging configuration settings for the event bus.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eb-event-bus-logs.html\">Configuring logs for event buses</a> in the <i>EventBridge User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEventBusResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "description" in value:
        out["Description"] = value["description"]
    if "dead_letter_config" in value:
        import aws_sdk_eventbridge.types.dead_letter_config

        out["DeadLetterConfig"] = (
            aws_sdk_eventbridge.types.dead_letter_config.serialize_aws_json_1_1(
                value["dead_letter_config"]
            )
        )
    if "log_config" in value:
        import aws_sdk_eventbridge.types.log_config

        out["LogConfig"] = aws_sdk_eventbridge.types.log_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEventBusResponse:
    out: UpdateEventBusResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeadLetterConfig" in data:
        import aws_sdk_eventbridge.types.dead_letter_config

        out["dead_letter_config"] = (
            aws_sdk_eventbridge.types.dead_letter_config.deserialize_aws_json_1_1(
                data["DeadLetterConfig"]
            )
        )
    if "LogConfig" in data:
        import aws_sdk_eventbridge.types.log_config

        out["log_config"] = (
            aws_sdk_eventbridge.types.log_config.deserialize_aws_json_1_1(
                data["LogConfig"]
            )
        )
    return out
