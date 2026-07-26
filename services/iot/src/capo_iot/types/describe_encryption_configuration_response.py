"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.configuration_details
    import capo_iot.types.date_type
    import capo_iot.types.encryption_type
    import capo_iot.types.kms_access_role_arn
    import capo_iot.types.kms_key_arn


class DescribeEncryptionConfigurationResponse(TypedDict, closed=True):
    encryption_type: NotRequired["capo_iot.types.encryption_type.EncryptionType"]
    """<p>The type of the KMS key.</p>"""
    kms_key_arn: NotRequired["capo_iot.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the customer managed KMS key.</p>"""
    kms_access_role_arn: NotRequired[
        "capo_iot.types.kms_access_role_arn.KmsAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role assumed by Amazon Web Services IoT Core to call KMS on behalf of the customer.</p>"""
    configuration_details: NotRequired[
        "capo_iot.types.configuration_details.ConfigurationDetails"
    ]
    """<p>The encryption configuration details that include the status information of the KMS key and the KMS access role.</p>"""
    last_modified_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date when encryption configuration is last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEncryptionConfigurationResponse) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import capo_iot.types.encryption_type

        out["encryptionType"] = capo_iot.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "kms_access_role_arn" in value:
        out["kmsAccessRoleArn"] = value["kms_access_role_arn"]
    if "configuration_details" in value:
        import capo_iot.types.configuration_details

        out["configurationDetails"] = (
            capo_iot.types.configuration_details.serialize_json(
                value["configuration_details"]
            )
        )
    if "last_modified_date" in value:
        import capo_iot.types.date_type

        out["lastModifiedDate"] = capo_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> DescribeEncryptionConfigurationResponse:
    out: DescribeEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import capo_iot.types.encryption_type

        out["encryption_type"] = capo_iot.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "kmsAccessRoleArn" in data:
        out["kms_access_role_arn"] = data["kmsAccessRoleArn"]
    if "configurationDetails" in data:
        import capo_iot.types.configuration_details

        out["configuration_details"] = (
            capo_iot.types.configuration_details.deserialize_json(
                data["configurationDetails"]
            )
        )
    if "lastModifiedDate" in data:
        import capo_iot.types.date_type

        out["last_modified_date"] = capo_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    return out
