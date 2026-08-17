"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_gpu_specification

ElasticGpuSpecificationList: TypeAlias = list[
    "capo_ec2.types.elastic_gpu_specification.ElasticGpuSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.elastic_gpu_specification

        capo_ec2.types.elastic_gpu_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ElasticGpuSpecificationList:
    import capo_ec2.types.elastic_gpu_specification

    out: ElasticGpuSpecificationList = []
    for child in el.findall("ElasticGpuSpecification"):
        out.append(
            capo_ec2.types.elastic_gpu_specification.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ElasticGpuSpecificationList:
    import capo_ec2.types.elastic_gpu_specification

    out: ElasticGpuSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.elastic_gpu_specification.deserialize_ec2_query(child)
        )
    return out
