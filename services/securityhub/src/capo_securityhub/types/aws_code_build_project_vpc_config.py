"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsCodeBuildProjectVpcConfig(TypedDict, closed=True):
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the VPC.</p>"""
    subnets: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of one or more subnet IDs in your VPC.</p>"""
    security_group_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of one or more security group IDs in your VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectVpcConfig) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnets" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Subnets"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["subnets"]
        )
    if "security_group_ids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SecurityGroupIds"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectVpcConfig:
    out: AwsCodeBuildProjectVpcConfig = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Subnets" in data:
        import capo_securityhub.types.non_empty_string_list

        out["subnets"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Subnets"]
        )
    if "SecurityGroupIds" in data:
        import capo_securityhub.types.non_empty_string_list

        out["security_group_ids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    return out
