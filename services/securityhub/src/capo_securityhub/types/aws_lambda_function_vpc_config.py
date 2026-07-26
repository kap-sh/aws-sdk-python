"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsLambdaFunctionVpcConfig(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of VPC security groups IDs.</p>"""
    subnet_ids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of VPC subnet IDs.</p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionVpcConfig) -> dict:
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
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionVpcConfig:
    out: AwsLambdaFunctionVpcConfig = {}  # type: ignore[typeddict-item]
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
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
