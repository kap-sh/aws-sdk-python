"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#EBSOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.integer_class
    import aws_sdk_elasticsearch_service.types.volume_type


class EBSOptions(TypedDict):
    ebs_enabled: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>Specifies whether EBS-based storage is enabled.</p>"""
    volume_type: NotRequired[
        "aws_sdk_elasticsearch_service.types.volume_type.VolumeType"
    ]
    """<p> Specifies the volume type for EBS-based storage.</p>"""
    volume_size: NotRequired[
        "aws_sdk_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p> Integer to specify the size of an EBS volume.</p>"""
    iops: NotRequired["aws_sdk_elasticsearch_service.types.integer_class.IntegerClass"]
    """<p>Specifies the IOPS for Provisioned IOPS And GP3 EBS volume (SSD).</p>"""
    throughput: NotRequired[
        "aws_sdk_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p>Specifies the Throughput for GP3 EBS volume (SSD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSOptions) -> dict:
    out: dict = {}
    if "ebs_enabled" in value:
        out["EBSEnabled"] = value["ebs_enabled"]
    if "volume_type" in value:
        import aws_sdk_elasticsearch_service.types.volume_type

        out["VolumeType"] = (
            aws_sdk_elasticsearch_service.types.volume_type.serialize_json(
                value["volume_type"]
            )
        )
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    return out


def deserialize_json(data: dict) -> EBSOptions:
    out: EBSOptions = {}  # type: ignore[typeddict-item]
    if "EBSEnabled" in data:
        out["ebs_enabled"] = data["EBSEnabled"]
    if "VolumeType" in data:
        import aws_sdk_elasticsearch_service.types.volume_type

        out["volume_type"] = (
            aws_sdk_elasticsearch_service.types.volume_type.deserialize_json(
                data["VolumeType"]
            )
        )
    if "VolumeSize" in data:
        out["volume_size"] = data["VolumeSize"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    return out
