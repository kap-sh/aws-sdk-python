"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEventBusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.dead_letter_config
    import aws_sdk_eventbridge.types.event_bus_description
    import aws_sdk_eventbridge.types.kms_key_identifier
    import aws_sdk_eventbridge.types.log_config
    import aws_sdk_eventbridge.types.string
    import aws_sdk_eventbridge.types.timestamp


class DescribeEventBusResponse(TypedDict):
    name: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The name of the event bus. Currently, this is always <code>default</code>.</p>"""
    arn: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the account permitted to write events to the current account.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    r"""<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt events on this event bus, if one has been specified.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html\">Data encryption in EventBridge</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_eventbridge.types.dead_letter_config.DeadLetterConfig"
    ]
    policy: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The policy that enables the external account to send events to your account.</p>"""
    log_config: NotRequired["aws_sdk_eventbridge.types.log_config.LogConfig"]
    r"""<p>The logging configuration settings for the event bus.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eb-event-bus-logs.html\">Configuring logs for event buses</a> in the <i>EventBridge User Guide</i>.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventBusResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "dead_letter_config" in value:
        import aws_sdk_eventbridge.types.dead_letter_config

        out["DeadLetterConfig"] = (
            aws_sdk_eventbridge.types.dead_letter_config.serialize_aws_json_1_1(
                value["dead_letter_config"]
            )
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "log_config" in value:
        import aws_sdk_eventbridge.types.log_config

        out["LogConfig"] = aws_sdk_eventbridge.types.log_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventBusResponse:
    out: DescribeEventBusResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if "DeadLetterConfig" in data:
        import aws_sdk_eventbridge.types.dead_letter_config

        out["dead_letter_config"] = (
            aws_sdk_eventbridge.types.dead_letter_config.deserialize_aws_json_1_1(
                data["DeadLetterConfig"]
            )
        )
    if "Policy" in data:
        out["policy"] = data["Policy"]
    if "LogConfig" in data:
        import aws_sdk_eventbridge.types.log_config

        out["log_config"] = (
            aws_sdk_eventbridge.types.log_config.deserialize_aws_json_1_1(
                data["LogConfig"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
