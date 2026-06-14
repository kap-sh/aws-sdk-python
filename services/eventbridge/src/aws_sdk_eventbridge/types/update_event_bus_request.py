"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateEventBusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.dead_letter_config
    import aws_sdk_eventbridge.types.event_bus_description
    import aws_sdk_eventbridge.types.event_bus_name
    import aws_sdk_eventbridge.types.kms_key_identifier
    import aws_sdk_eventbridge.types.log_config


class UpdateEventBusRequest(TypedDict):
    name: NotRequired["aws_sdk_eventbridge.types.event_bus_name.EventBusName"]
    """<p>The name of the event bus.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    r"""<p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on this event bus. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt events on the event bus.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html\">Identify and view keys</a> in the <i>Key Management Service Developer Guide</i>. </p> <note> <p>Schema discovery is not supported for event buses encrypted using a customer managed key. EventBridge returns an error if: </p> <ul> <li> <p>You call <code> <a href=\"https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers.html#CreateDiscoverer\">CreateDiscoverer</a> </code> on an event bus set to use a customer managed key for encryption.</p> </li> <li> <p>You call <code> <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdatedEventBus.html\">UpdatedEventBus</a> </code> to set a customer managed key on an event bus with schema discovery enabled.</p> </li> </ul> <p>To enable schema discovery on an event bus, choose to use an Amazon Web Services owned key. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-cmkey.html\">Encrypting events</a> in the <i>Amazon EventBridge User Guide</i>.</p> </note> <important> <p>If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html\">Encrypting archives</a> in the <i>Amazon EventBridge User Guide</i>.</p> </important>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_eventbridge.types.dead_letter_config.DeadLetterConfig"
    ]
    log_config: NotRequired["aws_sdk_eventbridge.types.log_config.LogConfig"]
    r"""<p>The logging configuration settings for the event bus.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eb-event-bus-logs.html\">Configuring logs for event buses</a> in the <i>EventBridge User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEventBusRequest) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> UpdateEventBusRequest:
    out: UpdateEventBusRequest = {}  # type: ignore[typeddict-item]
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
