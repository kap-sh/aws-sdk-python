"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRetentionConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.retention_configuration_list


class DescribeRetentionConfigurationsResponse(TypedDict):
    retention_configurations: NotRequired[
        "aws_sdk_config_service.types.retention_configuration_list.RetentionConfigurationList"
    ]
    """<p>Returns a retention configuration object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRetentionConfigurationsResponse) -> dict:
    out: dict = {}
    if "retention_configurations" in value:
        import aws_sdk_config_service.types.retention_configuration_list

        out["RetentionConfigurations"] = (
            aws_sdk_config_service.types.retention_configuration_list.serialize_aws_json_1_1(
                value["retention_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRetentionConfigurationsResponse:
    out: DescribeRetentionConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "RetentionConfigurations" in data:
        import aws_sdk_config_service.types.retention_configuration_list

        out["retention_configurations"] = (
            aws_sdk_config_service.types.retention_configuration_list.deserialize_aws_json_1_1(
                data["RetentionConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
