"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationRecorderStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.configuration_recorder_name_list
    import capo_config_service.types.service_principal


class DescribeConfigurationRecorderStatusRequest(TypedDict, closed=True):
    configuration_recorder_names: NotRequired[
        "capo_config_service.types.configuration_recorder_name_list.ConfigurationRecorderNameList"
    ]
    """<p>The name of the configuration recorder. If the name is not specified, the operation returns the status for the customer managed configuration recorder configured for the account, if applicable.</p> <note> <p>When making a request to this operation, you can only specify one configuration recorder.</p> </note>"""
    service_principal: NotRequired[
        "capo_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, you can use the service principal of the linked Amazon Web Services service to specify the configuration recorder.</p>"""
    arn: NotRequired[
        "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the configuration recorder that you want to specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationRecorderStatusRequest) -> dict:
    out: dict = {}
    if "configuration_recorder_names" in value:
        import capo_config_service.types.configuration_recorder_name_list

        out["ConfigurationRecorderNames"] = (
            capo_config_service.types.configuration_recorder_name_list.serialize_aws_json_1_1(
                value["configuration_recorder_names"]
            )
        )
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationRecorderStatusRequest:
    out: DescribeConfigurationRecorderStatusRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorderNames" in data:
        import capo_config_service.types.configuration_recorder_name_list

        out["configuration_recorder_names"] = (
            capo_config_service.types.configuration_recorder_name_list.deserialize_aws_json_1_1(
                data["ConfigurationRecorderNames"]
            )
        )
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
