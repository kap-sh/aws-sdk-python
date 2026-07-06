"""Generated from Smithy shape ``com.amazonaws.opensearch#EBSOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.integer_class
    import aws_sdk_opensearch.types.volume_type


class EBSOptions(TypedDict, closed=True):
    ebs_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether EBS volumes are attached to data nodes in an OpenSearch Service domain.</p>"""
    volume_type: NotRequired["aws_sdk_opensearch.types.volume_type.VolumeType"]
    """<p>Specifies the type of EBS volumes attached to data nodes.</p>"""
    volume_size: NotRequired["aws_sdk_opensearch.types.integer_class.IntegerClass"]
    """<p>Specifies the size (in GiB) of EBS volumes attached to data nodes.</p>"""
    iops: NotRequired["aws_sdk_opensearch.types.integer_class.IntegerClass"]
    """<p>Specifies the baseline input/output (I/O) performance of EBS volumes attached to data nodes. Applicable only for the <code>gp3</code> and provisioned IOPS EBS volume types.</p>"""
    throughput: NotRequired["aws_sdk_opensearch.types.integer_class.IntegerClass"]
    """<p>Specifies the throughput (in MiB/s) of the EBS volumes attached to data nodes. Applicable only for the <code>gp3</code> volume type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSOptions) -> dict:
    out: dict = {}
    if "ebs_enabled" in value:
        out["EBSEnabled"] = value["ebs_enabled"]
    if "volume_type" in value:
        import aws_sdk_opensearch.types.volume_type

        out["VolumeType"] = aws_sdk_opensearch.types.volume_type.serialize_json(
            value["volume_type"]
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
        import aws_sdk_opensearch.types.volume_type

        out["volume_type"] = aws_sdk_opensearch.types.volume_type.deserialize_json(
            data["VolumeType"]
        )
    if "VolumeSize" in data:
        out["volume_size"] = data["VolumeSize"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    return out
