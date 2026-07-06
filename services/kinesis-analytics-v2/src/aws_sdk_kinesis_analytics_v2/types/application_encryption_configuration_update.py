"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationEncryptionConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.key_id
    import aws_sdk_kinesis_analytics_v2.types.key_type


class ApplicationEncryptionConfigurationUpdate(TypedDict, closed=True):
    key_id_update: NotRequired["aws_sdk_kinesis_analytics_v2.types.key_id.KeyId"]
    """<p>The key ARN, key ID, alias ARN, or alias name of the KMS key to be used for encryption at rest.</p>"""
    key_type_update: "aws_sdk_kinesis_analytics_v2.types.key_type.KeyType"
    """<p>Specifies the type of key to be used for encryption at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationEncryptionConfigurationUpdate) -> dict:
    out: dict = {}
    if "key_id_update" in value:
        out["KeyIdUpdate"] = value["key_id_update"]
    import aws_sdk_kinesis_analytics_v2.types.key_type

    out["KeyTypeUpdate"] = (
        aws_sdk_kinesis_analytics_v2.types.key_type.serialize_aws_json_1_1(
            value["key_type_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationEncryptionConfigurationUpdate:
    out: ApplicationEncryptionConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "KeyIdUpdate" in data:
        out["key_id_update"] = data["KeyIdUpdate"]
    if "KeyTypeUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.key_type

        out["key_type_update"] = (
            aws_sdk_kinesis_analytics_v2.types.key_type.deserialize_aws_json_1_1(
                data["KeyTypeUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationEncryptionConfigurationUpdate.key_type_update required"
        )
    return out
