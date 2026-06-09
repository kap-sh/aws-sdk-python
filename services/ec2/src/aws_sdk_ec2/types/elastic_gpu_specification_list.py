"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_specification

ElasticGpuSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_gpu_specification.ElasticGpuSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.elastic_gpu_specification

        aws_sdk_ec2.types.elastic_gpu_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ElasticGpuSpecificationList:
    import aws_sdk_ec2.types.elastic_gpu_specification

    out: ElasticGpuSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.elastic_gpu_specification.deserialize_ec2_query(child)
        )
    return out
