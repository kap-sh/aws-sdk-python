"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpus

ElasticGpuSet: TypeAlias = list["aws_sdk_ec2.types.elastic_gpus.ElasticGpus"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.elastic_gpus

        aws_sdk_ec2.types.elastic_gpus.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ElasticGpuSet:
    import aws_sdk_ec2.types.elastic_gpus

    out: ElasticGpuSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.elastic_gpus.deserialize_ec2_query(child))
    return out
