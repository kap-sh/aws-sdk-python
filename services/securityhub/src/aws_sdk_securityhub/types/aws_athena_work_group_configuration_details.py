"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAthenaWorkGroupConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_details


class AwsAthenaWorkGroupConfigurationDetails(TypedDict):
    result_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_details.AwsAthenaWorkGroupConfigurationResultConfigurationDetails"
    ]
    """<p> The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query and calculation results. These are known as client-side settings. If workgroup settings override client-side settings, then the query uses the workgroup settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAthenaWorkGroupConfigurationDetails) -> dict:
    out: dict = {}
    if "result_configuration" in value:
        import aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_details

        out["ResultConfiguration"] = (
            aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_details.serialize_json(
                value["result_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsAthenaWorkGroupConfigurationDetails:
    out: AwsAthenaWorkGroupConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "ResultConfiguration" in data:
        import aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_details

        out["result_configuration"] = (
            aws_sdk_securityhub.types.aws_athena_work_group_configuration_result_configuration_details.deserialize_json(
                data["ResultConfiguration"]
            )
        )
    return out
