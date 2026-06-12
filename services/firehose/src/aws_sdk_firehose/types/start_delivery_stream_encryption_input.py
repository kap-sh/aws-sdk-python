"""Generated from Smithy shape ``com.amazonaws.firehose#StartDeliveryStreamEncryptionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_encryption_configuration_input
    import aws_sdk_firehose.types.delivery_stream_name


class StartDeliveryStreamEncryptionInput(TypedDict):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream for which you want to enable server-side encryption (SSE).</p>"""
    delivery_stream_encryption_configuration_input: NotRequired[
        "aws_sdk_firehose.types.delivery_stream_encryption_configuration_input.DeliveryStreamEncryptionConfigurationInput"
    ]
    """<p>Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDeliveryStreamEncryptionInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "delivery_stream_encryption_configuration_input" in value:
        import aws_sdk_firehose.types.delivery_stream_encryption_configuration_input

        out["DeliveryStreamEncryptionConfigurationInput"] = (
            aws_sdk_firehose.types.delivery_stream_encryption_configuration_input.serialize_aws_json_1_1(
                value["delivery_stream_encryption_configuration_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDeliveryStreamEncryptionInput:
    out: StartDeliveryStreamEncryptionInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "StartDeliveryStreamEncryptionInput.delivery_stream_name required"
        )
    if "DeliveryStreamEncryptionConfigurationInput" in data:
        import aws_sdk_firehose.types.delivery_stream_encryption_configuration_input

        out["delivery_stream_encryption_configuration_input"] = (
            aws_sdk_firehose.types.delivery_stream_encryption_configuration_input.deserialize_aws_json_1_1(
                data["DeliveryStreamEncryptionConfigurationInput"]
            )
        )
    return out
