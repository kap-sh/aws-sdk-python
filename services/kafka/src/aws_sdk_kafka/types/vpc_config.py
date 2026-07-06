"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string


class VpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>The IDs of the subnets associated with the cluster.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The IDs of the security groups associated with the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["subnetIds"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["securityGroupIds"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["security_group_ids"]
        )
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["subnet_ids"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["security_group_ids"] = (
            aws_sdk_kafka.types.__list_of__string.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
