"""Generated from Smithy shape ``com.amazonaws.kafka#EBSStorageInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer_min1_max16384
    import aws_sdk_kafka.types.provisioned_throughput


class EBSStorageInfo(TypedDict, closed=True):
    provisioned_throughput: NotRequired[
        "aws_sdk_kafka.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>EBS volume provisioned throughput information.</p>"""
    volume_size: NotRequired[
        "aws_sdk_kafka.types.__integer_min1_max16384.__integerMin1Max16384"
    ]
    """<p>The size in GiB of the EBS volume for the data drive on each broker node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSStorageInfo) -> dict:
    out: dict = {}
    if "provisioned_throughput" in value:
        import aws_sdk_kafka.types.provisioned_throughput

        out["provisionedThroughput"] = (
            aws_sdk_kafka.types.provisioned_throughput.serialize_json(
                value["provisioned_throughput"]
            )
        )
    if "volume_size" in value:
        out["volumeSize"] = value["volume_size"]
    return out


def deserialize_json(data: dict) -> EBSStorageInfo:
    out: EBSStorageInfo = {}  # type: ignore[typeddict-item]
    if "provisionedThroughput" in data:
        import aws_sdk_kafka.types.provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_kafka.types.provisioned_throughput.deserialize_json(
                data["provisionedThroughput"]
            )
        )
    if "volumeSize" in data:
        out["volume_size"] = data["volumeSize"]
    return out
