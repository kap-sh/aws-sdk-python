"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#InstanceHealthList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.single_instance_health

InstanceHealthList: TypeAlias = list[
    "capo_elastic_beanstalk.types.single_instance_health.SingleInstanceHealth"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceHealthList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.single_instance_health

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.single_instance_health.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstanceHealthList:
    import capo_elastic_beanstalk.types.single_instance_health

    out: InstanceHealthList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.single_instance_health.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: InstanceHealthList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.single_instance_health

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.single_instance_health.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstanceHealthList:
    import capo_elastic_beanstalk.types.single_instance_health

    out: InstanceHealthList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.single_instance_health.deserialize_query(child)
        )
    return out
