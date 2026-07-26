"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainVpcOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string_list


class AwsOpenSearchServiceDomainVpcOptionsDetails(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of security group IDs that are associated with the VPC endpoints for the domain.</p>"""
    subnet_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of subnet IDs that are associated with the VPC endpoints for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOpenSearchServiceDomainVpcOptionsDetails) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SecurityGroupIds"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SubnetIds"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["subnet_ids"]
        )
    return out


def deserialize_json(data: dict) -> AwsOpenSearchServiceDomainVpcOptionsDetails:
    out: AwsOpenSearchServiceDomainVpcOptionsDetails = {}  # type: ignore[typeddict-item]
    if "SecurityGroupIds" in data:
        import capo_securityhub.types.non_empty_string_list

        out["security_group_ids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "SubnetIds" in data:
        import capo_securityhub.types.non_empty_string_list

        out["subnet_ids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SubnetIds"]
            )
        )
    return out
