"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainVpcOptionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsOpenSearchServiceDomainVpcOptionsDetails(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of security group IDs that are associated with the VPC endpoints for the domain.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of subnet IDs that are associated with the VPC endpoints for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOpenSearchServiceDomainVpcOptionsDetails) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> AwsOpenSearchServiceDomainVpcOptionsDetails:
    out: AwsOpenSearchServiceDomainVpcOptionsDetails = {}  # type: ignore[typeddict-item]
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
    return out
