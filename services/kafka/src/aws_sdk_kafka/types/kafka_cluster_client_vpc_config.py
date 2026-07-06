"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterClientVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string


class KafkaClusterClientVpcConfig(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The security groups to attach to the ENIs for the broker nodes.</p>"""
    subnet_ids: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>The list of subnets in the client VPC to connect to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterClientVpcConfig) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["securityGroupIds"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["security_group_ids"]
        )
    if "subnet_ids" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["subnetIds"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["subnet_ids"]
        )
    return out


def deserialize_json(data: dict) -> KafkaClusterClientVpcConfig:
    out: KafkaClusterClientVpcConfig = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["security_group_ids"] = (
            aws_sdk_kafka.types.__list_of__string.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["subnet_ids"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["subnetIds"]
        )
    return out
