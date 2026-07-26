"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRetentionConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.next_token
    import capo_config_service.types.retention_configuration_name_list


class DescribeRetentionConfigurationsRequest(TypedDict, closed=True):
    retention_configuration_names: NotRequired[
        "capo_config_service.types.retention_configuration_name_list.RetentionConfigurationNameList"
    ]
    """<p>A list of names of retention configurations for which you want details. If you do not specify a name, Config returns details for all the retention configurations for that account.</p> <note> <p>Currently, Config supports only one retention configuration per region in your account.</p> </note>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRetentionConfigurationsRequest) -> dict:
    out: dict = {}
    if "retention_configuration_names" in value:
        import capo_config_service.types.retention_configuration_name_list

        out["RetentionConfigurationNames"] = (
            capo_config_service.types.retention_configuration_name_list.serialize_aws_json_1_1(
                value["retention_configuration_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRetentionConfigurationsRequest:
    out: DescribeRetentionConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "RetentionConfigurationNames" in data:
        import capo_config_service.types.retention_configuration_name_list

        out["retention_configuration_names"] = (
            capo_config_service.types.retention_configuration_name_list.deserialize_aws_json_1_1(
                data["RetentionConfigurationNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
