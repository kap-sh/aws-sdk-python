"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_gpu_association

ElasticGpuAssociationList: TypeAlias = list[
    "capo_ec2.types.elastic_gpu_association.ElasticGpuAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.elastic_gpu_association

        capo_ec2.types.elastic_gpu_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ElasticGpuAssociationList:
    import capo_ec2.types.elastic_gpu_association

    out: ElasticGpuAssociationList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.elastic_gpu_association.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ElasticGpuAssociationList:
    import capo_ec2.types.elastic_gpu_association

    out: ElasticGpuAssociationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.elastic_gpu_association.deserialize_ec2_query(child))
    return out
