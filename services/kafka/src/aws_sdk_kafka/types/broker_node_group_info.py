"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerNodeGroupInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string_min5_max32
    import aws_sdk_kafka.types.broker_az_distribution
    import aws_sdk_kafka.types.connectivity_info
    import aws_sdk_kafka.types.storage_info


class BrokerNodeGroupInfo(TypedDict):
    broker_az_distribution: NotRequired[
        "aws_sdk_kafka.types.broker_az_distribution.BrokerAZDistribution"
    ]
    """<p>The distribution of broker nodes across Availability Zones. This is an optional parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this parameter to the value DEFAULT. No other values are currently allowed.</p> <p>Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to the subnets you provide when you create the cluster.</p>"""
    client_subnets: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can't occupy the Availability Zone with ID use use1-az3.</p>"""
    instance_type: NotRequired[
        "aws_sdk_kafka.types.__string_min5_max32.__stringMin5Max32"
    ]
    """<p>The type of Amazon EC2 instances to use for Apache Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.</p>"""
    security_groups: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC.</p>"""
    storage_info: NotRequired["aws_sdk_kafka.types.storage_info.StorageInfo"]
    """<p>Contains information about storage volumes attached to MSK broker nodes.</p>"""
    connectivity_info: NotRequired[
        "aws_sdk_kafka.types.connectivity_info.ConnectivityInfo"
    ]
    """<p>Information about the broker access configuration.</p>"""
    zone_ids: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>The list of zoneIds for the cluster in the virtual private cloud (VPC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerNodeGroupInfo) -> dict:
    out: dict = {}
    if "broker_az_distribution" in value:
        import aws_sdk_kafka.types.broker_az_distribution

        out["brokerAZDistribution"] = (
            aws_sdk_kafka.types.broker_az_distribution.serialize_json(
                value["broker_az_distribution"]
            )
        )
    if "client_subnets" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["clientSubnets"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["client_subnets"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "security_groups" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["securityGroups"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["security_groups"]
        )
    if "storage_info" in value:
        import aws_sdk_kafka.types.storage_info

        out["storageInfo"] = aws_sdk_kafka.types.storage_info.serialize_json(
            value["storage_info"]
        )
    if "connectivity_info" in value:
        import aws_sdk_kafka.types.connectivity_info

        out["connectivityInfo"] = aws_sdk_kafka.types.connectivity_info.serialize_json(
            value["connectivity_info"]
        )
    if "zone_ids" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["zoneIds"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["zone_ids"]
        )
    return out


def deserialize_json(data: dict) -> BrokerNodeGroupInfo:
    out: BrokerNodeGroupInfo = {}  # type: ignore[typeddict-item]
    if "brokerAZDistribution" in data:
        import aws_sdk_kafka.types.broker_az_distribution

        out["broker_az_distribution"] = (
            aws_sdk_kafka.types.broker_az_distribution.deserialize_json(
                data["brokerAZDistribution"]
            )
        )
    if "clientSubnets" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["client_subnets"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["clientSubnets"]
        )
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "securityGroups" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["security_groups"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["securityGroups"]
        )
    if "storageInfo" in data:
        import aws_sdk_kafka.types.storage_info

        out["storage_info"] = aws_sdk_kafka.types.storage_info.deserialize_json(
            data["storageInfo"]
        )
    if "connectivityInfo" in data:
        import aws_sdk_kafka.types.connectivity_info

        out["connectivity_info"] = (
            aws_sdk_kafka.types.connectivity_info.deserialize_json(
                data["connectivityInfo"]
            )
        )
    if "zoneIds" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["zone_ids"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["zoneIds"]
        )
    return out
