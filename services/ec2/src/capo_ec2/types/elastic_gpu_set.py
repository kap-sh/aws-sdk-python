"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_gpus

ElasticGpuSet: TypeAlias = list["capo_ec2.types.elastic_gpus.ElasticGpus"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.elastic_gpus

        capo_ec2.types.elastic_gpus.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> ElasticGpuSet:
    import capo_ec2.types.elastic_gpus

    out: ElasticGpuSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.elastic_gpus.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ElasticGpuSet:
    import capo_ec2.types.elastic_gpus

    out: ElasticGpuSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.elastic_gpus.deserialize_ec2_query(child))
    return out
