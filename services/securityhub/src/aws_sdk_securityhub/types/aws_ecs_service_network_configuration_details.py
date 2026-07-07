"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceNetworkConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_service_network_configuration_aws_vpc_configuration_details


class AwsEcsServiceNetworkConfigurationDetails(TypedDict, closed=True):
    aws_vpc_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_service_network_configuration_aws_vpc_configuration_details.AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails"
    ]
    """<p>The VPC subnet and security group configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceNetworkConfigurationDetails) -> dict:
    out: dict = {}
    if "aws_vpc_configuration" in value:
        import aws_sdk_securityhub.types.aws_ecs_service_network_configuration_aws_vpc_configuration_details

        out["AwsVpcConfiguration"] = (
            aws_sdk_securityhub.types.aws_ecs_service_network_configuration_aws_vpc_configuration_details.serialize_json(
                value["aws_vpc_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEcsServiceNetworkConfigurationDetails:
    out: AwsEcsServiceNetworkConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "AwsVpcConfiguration" in data:
        import aws_sdk_securityhub.types.aws_ecs_service_network_configuration_aws_vpc_configuration_details

        out["aws_vpc_configuration"] = (
            aws_sdk_securityhub.types.aws_ecs_service_network_configuration_aws_vpc_configuration_details.deserialize_json(
                data["AwsVpcConfiguration"]
            )
        )
    return out
