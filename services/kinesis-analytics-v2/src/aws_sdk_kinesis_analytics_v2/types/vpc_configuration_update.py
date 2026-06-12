"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.id
    import aws_sdk_kinesis_analytics_v2.types.security_group_ids
    import aws_sdk_kinesis_analytics_v2.types.subnet_ids


class VpcConfigurationUpdate(TypedDict):
    vpc_configuration_id: "aws_sdk_kinesis_analytics_v2.types.id.Id"
    """<p>Describes an update to the ID of the VPC configuration.</p>"""
    subnet_id_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.subnet_ids.SubnetIds"
    ]
    """<p>Describes updates to the array of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html\">Subnet</a> IDs used by the VPC configuration.</p>"""
    security_group_id_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>Describes updates to the array of <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html\">SecurityGroup</a> IDs used by the VPC configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfigurationUpdate) -> dict:
    out: dict = {}
    out["VpcConfigurationId"] = value["vpc_configuration_id"]
    if "subnet_id_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.subnet_ids

        out["SubnetIdUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.subnet_ids.serialize_aws_json_1_1(
                value["subnet_id_updates"]
            )
        )
    if "security_group_id_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.security_group_ids

        out["SecurityGroupIdUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_id_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfigurationUpdate:
    out: VpcConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "VpcConfigurationId" in data:
        out["vpc_configuration_id"] = data["VpcConfigurationId"]
    else:
        raise DeserializationError(
            "VpcConfigurationUpdate.vpc_configuration_id required"
        )
    if "SubnetIdUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.subnet_ids

        out["subnet_id_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIdUpdates"]
            )
        )
    if "SecurityGroupIdUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.security_group_ids

        out["security_group_id_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIdUpdates"]
            )
        )
    return out
