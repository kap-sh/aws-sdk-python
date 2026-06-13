"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_odb.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.aws_encryption_key_configuration
    import aws_sdk_odb.types.oci_encryption_key_configuration
    import aws_sdk_odb.types.okv_encryption_key_configuration


class _EncryptionKeyConfiguration_awsEncryptionKey(TypedDict):
    awsEncryptionKey: "aws_sdk_odb.types.aws_encryption_key_configuration.AwsEncryptionKeyConfiguration"


class _EncryptionKeyConfiguration_ociEncryptionKey(TypedDict):
    ociEncryptionKey: "aws_sdk_odb.types.oci_encryption_key_configuration.OciEncryptionKeyConfiguration"


class _EncryptionKeyConfiguration_okvEncryptionKey(TypedDict):
    okvEncryptionKey: "aws_sdk_odb.types.okv_encryption_key_configuration.OkvEncryptionKeyConfiguration"


EncryptionKeyConfiguration: TypeAlias = (
    _EncryptionKeyConfiguration_awsEncryptionKey
    | _EncryptionKeyConfiguration_ociEncryptionKey
    | _EncryptionKeyConfiguration_okvEncryptionKey
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionKeyConfiguration) -> dict:
    if "awsEncryptionKey" in value:
        import aws_sdk_odb.types.aws_encryption_key_configuration

        return {
            "awsEncryptionKey": aws_sdk_odb.types.aws_encryption_key_configuration.serialize_aws_json_1_0(
                value["awsEncryptionKey"]
            )
        }
    elif "ociEncryptionKey" in value:
        import aws_sdk_odb.types.oci_encryption_key_configuration

        return {
            "ociEncryptionKey": aws_sdk_odb.types.oci_encryption_key_configuration.serialize_aws_json_1_0(
                value["ociEncryptionKey"]
            )
        }
    elif "okvEncryptionKey" in value:
        import aws_sdk_odb.types.okv_encryption_key_configuration

        return {
            "okvEncryptionKey": aws_sdk_odb.types.okv_encryption_key_configuration.serialize_aws_json_1_0(
                value["okvEncryptionKey"]
            )
        }
    else:
        raise SerializationError("EncryptionKeyConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionKeyConfiguration:
    if "awsEncryptionKey" in data:
        import aws_sdk_odb.types.aws_encryption_key_configuration

        return {
            "awsEncryptionKey": aws_sdk_odb.types.aws_encryption_key_configuration.deserialize_aws_json_1_0(
                data["awsEncryptionKey"]
            )
        }
    elif "ociEncryptionKey" in data:
        import aws_sdk_odb.types.oci_encryption_key_configuration

        return {
            "ociEncryptionKey": aws_sdk_odb.types.oci_encryption_key_configuration.deserialize_aws_json_1_0(
                data["ociEncryptionKey"]
            )
        }
    elif "okvEncryptionKey" in data:
        import aws_sdk_odb.types.okv_encryption_key_configuration

        return {
            "okvEncryptionKey": aws_sdk_odb.types.okv_encryption_key_configuration.deserialize_aws_json_1_0(
                data["okvEncryptionKey"]
            )
        }
    else:
        raise DeserializationError(
            "EncryptionKeyConfiguration: no recognized variant key"
        )
