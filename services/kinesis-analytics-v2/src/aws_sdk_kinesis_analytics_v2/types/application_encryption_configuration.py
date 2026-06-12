"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.key_id
    import aws_sdk_kinesis_analytics_v2.types.key_type


class ApplicationEncryptionConfiguration(TypedDict):
    key_id: NotRequired["aws_sdk_kinesis_analytics_v2.types.key_id.KeyId"]
    """<p>The key ARN, key ID, alias ARN, or alias name of the KMS key used for encryption at rest.</p>"""
    key_type: "aws_sdk_kinesis_analytics_v2.types.key_type.KeyType"
    """<p>Specifies the type of key used for encryption at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationEncryptionConfiguration) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    import aws_sdk_kinesis_analytics_v2.types.key_type

    out["KeyType"] = aws_sdk_kinesis_analytics_v2.types.key_type.serialize_aws_json_1_1(
        value["key_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationEncryptionConfiguration:
    out: ApplicationEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyType" in data:
        import aws_sdk_kinesis_analytics_v2.types.key_type

        out["key_type"] = (
            aws_sdk_kinesis_analytics_v2.types.key_type.deserialize_aws_json_1_1(
                data["KeyType"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationEncryptionConfiguration.key_type required"
        )
    return out
