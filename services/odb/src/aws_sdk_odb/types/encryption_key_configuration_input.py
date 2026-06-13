"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_odb.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.aws_encryption_key_configuration_input


class _EncryptionKeyConfigurationInput_awsEncryptionKey(TypedDict):
    awsEncryptionKey: "aws_sdk_odb.types.aws_encryption_key_configuration_input.AwsEncryptionKeyConfigurationInput"


EncryptionKeyConfigurationInput: TypeAlias = (
    _EncryptionKeyConfigurationInput_awsEncryptionKey
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionKeyConfigurationInput) -> dict:
    if "awsEncryptionKey" in value:
        import aws_sdk_odb.types.aws_encryption_key_configuration_input

        return {
            "awsEncryptionKey": aws_sdk_odb.types.aws_encryption_key_configuration_input.serialize_aws_json_1_0(
                value["awsEncryptionKey"]
            )
        }
    else:
        raise SerializationError("EncryptionKeyConfigurationInput: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionKeyConfigurationInput:
    if "awsEncryptionKey" in data:
        import aws_sdk_odb.types.aws_encryption_key_configuration_input

        return {
            "awsEncryptionKey": aws_sdk_odb.types.aws_encryption_key_configuration_input.deserialize_aws_json_1_0(
                data["awsEncryptionKey"]
            )
        }
    else:
        raise DeserializationError(
            "EncryptionKeyConfigurationInput: no recognized variant key"
        )
