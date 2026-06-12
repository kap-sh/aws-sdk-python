"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRetentionConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.retention_configuration_name_list


class DescribeRetentionConfigurationsRequest(TypedDict):
    retention_configuration_names: NotRequired[
        "aws_sdk_config_service.types.retention_configuration_name_list.RetentionConfigurationNameList"
    ]
    """<p>A list of names of retention configurations for which you want details. If you do not specify a name, Config returns details for all the retention configurations for that account.</p> <note> <p>Currently, Config supports only one retention configuration per region in your account.</p> </note>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRetentionConfigurationsRequest) -> dict:
    out: dict = {}
    if "retention_configuration_names" in value:
        import aws_sdk_config_service.types.retention_configuration_name_list

        out["RetentionConfigurationNames"] = (
            aws_sdk_config_service.types.retention_configuration_name_list.serialize_aws_json_1_1(
                value["retention_configuration_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRetentionConfigurationsRequest:
    out: DescribeRetentionConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "RetentionConfigurationNames" in data:
        import aws_sdk_config_service.types.retention_configuration_name_list

        out["retention_configuration_names"] = (
            aws_sdk_config_service.types.retention_configuration_name_list.deserialize_aws_json_1_1(
                data["RetentionConfigurationNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
