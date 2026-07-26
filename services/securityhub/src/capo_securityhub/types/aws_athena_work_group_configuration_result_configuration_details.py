"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAthenaWorkGroupConfigurationResultConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details


class AwsAthenaWorkGroupConfigurationResultConfigurationDetails(TypedDict, closed=True):
    encryption_configuration: NotRequired[
        "capo_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details.AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails"
    ]
    """<p> Specifies the method used to encrypt the user’s data stores in the Athena workgroup. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAthenaWorkGroupConfigurationResultConfigurationDetails,
) -> dict:
    out: dict = {}
    if "encryption_configuration" in value:
        import capo_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details

        out["EncryptionConfiguration"] = (
            capo_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsAthenaWorkGroupConfigurationResultConfigurationDetails:
    out: AwsAthenaWorkGroupConfigurationResultConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionConfiguration" in data:
        import capo_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details

        out["encryption_configuration"] = (
            capo_securityhub.types.aws_athena_work_group_configuration_result_configuration_encryption_configuration_details.deserialize_json(
                data["EncryptionConfiguration"]
            )
        )
    return out
