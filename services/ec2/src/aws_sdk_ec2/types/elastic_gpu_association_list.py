"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_association

ElasticGpuAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_gpu_association.ElasticGpuAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.elastic_gpu_association

        aws_sdk_ec2.types.elastic_gpu_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ElasticGpuAssociationList:
    import aws_sdk_ec2.types.elastic_gpu_association

    out: ElasticGpuAssociationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.elastic_gpu_association.deserialize_ec2_query(child)
        )
    return out
