"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.security_group_ids
    import aws_sdk_kinesis_analytics_v2.types.subnet_ids


class VpcConfiguration(TypedDict):
    subnet_ids: "aws_sdk_kinesis_analytics_v2.types.subnet_ids.SubnetIds"
    r"""<p>The array of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html\">Subnet</a> IDs used by the VPC configuration.</p>"""
    security_group_ids: (
        "aws_sdk_kinesis_analytics_v2.types.security_group_ids.SecurityGroupIds"
    )
    r"""<p>The array of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html\">SecurityGroup</a> IDs used by the VPC configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.subnet_ids

    out["SubnetIds"] = (
        aws_sdk_kinesis_analytics_v2.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    import aws_sdk_kinesis_analytics_v2.types.security_group_ids

    out["SecurityGroupIds"] = (
        aws_sdk_kinesis_analytics_v2.types.security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_kinesis_analytics_v2.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_kinesis_analytics_v2.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.subnet_ids required")
    if "SecurityGroupIds" in data:
        import aws_sdk_kinesis_analytics_v2.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_kinesis_analytics_v2.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.security_group_ids required")
    return out
