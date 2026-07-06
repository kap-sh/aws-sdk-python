"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationRecordersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.configuration_recorder_name_list
    import aws_sdk_config_service.types.service_principal


class DescribeConfigurationRecordersRequest(TypedDict, closed=True):
    configuration_recorder_names: NotRequired[
        "aws_sdk_config_service.types.configuration_recorder_name_list.ConfigurationRecorderNameList"
    ]
    """<p>A list of names of the configuration recorders that you want to specify.</p> <note> <p>When making a request to this operation, you can only specify one configuration recorder.</p> </note>"""
    service_principal: NotRequired[
        "aws_sdk_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, you can use the service principal of the linked Amazon Web Services service to specify the configuration recorder.</p>"""
    arn: NotRequired[
        "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the configuration recorder that you want to specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationRecordersRequest) -> dict:
    out: dict = {}
    if "configuration_recorder_names" in value:
        import aws_sdk_config_service.types.configuration_recorder_name_list

        out["ConfigurationRecorderNames"] = (
            aws_sdk_config_service.types.configuration_recorder_name_list.serialize_aws_json_1_1(
                value["configuration_recorder_names"]
            )
        )
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationRecordersRequest:
    out: DescribeConfigurationRecordersRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorderNames" in data:
        import aws_sdk_config_service.types.configuration_recorder_name_list

        out["configuration_recorder_names"] = (
            aws_sdk_config_service.types.configuration_recorder_name_list.deserialize_aws_json_1_1(
                data["ConfigurationRecorderNames"]
            )
        )
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
