"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcEndpointServiceServiceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_details

AwsEc2VpcEndpointServiceServiceTypeList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_details.AwsEc2VpcEndpointServiceServiceTypeDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcEndpointServiceServiceTypeList) -> list:
    import capo_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2VpcEndpointServiceServiceTypeList:
    import capo_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_details

    out: AwsEc2VpcEndpointServiceServiceTypeList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_details.deserialize_json(
                item
            )
        )
    return out
