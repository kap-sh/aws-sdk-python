"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainVPCOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsElasticsearchDomainVPCOptions(TypedDict, closed=True):
    availability_zones: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of Availability Zones associated with the VPC subnets.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of security group IDs associated with the VPC endpoints for the domain.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of subnet IDs associated with the VPC endpoints for the domain.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>ID for the VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainVPCOptions) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["AvailabilityZones"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["availability_zones"]
            )
        )
    if "security_group_ids" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["SecurityGroupIds"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["SubnetIds"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["subnet_ids"]
            )
        )
    if "vpc_id" in value:
        out["VPCId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainVPCOptions:
    out: AwsElasticsearchDomainVPCOptions = {}  # type: ignore[typeddict-item]
    if "AvailabilityZones" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["availability_zones"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if "SecurityGroupIds" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["security_group_ids"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "SubnetIds" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["subnet_ids"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["SubnetIds"]
            )
        )
    if "VPCId" in data:
        out["vpc_id"] = data["VPCId"]
    return out
