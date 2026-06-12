"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAthenaWorkGroupConfigurationResultConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details


class AwsAthenaWorkGroupConfigurationResultConfigurationDetails(TypedDict):
    encryption_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details.AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails"
    ]
    """<p> Specifies the method used to encrypt the user’s data stores in the Athena workgroup. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAthenaWorkGroupConfigurationResultConfigurationDetails,
) -> dict:
    out: dict = {}
    if "encryption_configuration" in value:
        import aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details

        out["EncryptionConfiguration"] = (
            aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsAthenaWorkGroupConfigurationResultConfigurationDetails:
    out: AwsAthenaWorkGroupConfigurationResultConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionConfiguration" in data:
        import aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details

        out["encryption_configuration"] = (
            aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details.deserialize_json(
                data["EncryptionConfiguration"]
            )
        )
    return out
