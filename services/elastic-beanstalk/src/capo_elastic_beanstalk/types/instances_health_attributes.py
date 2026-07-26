"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#InstancesHealthAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.instances_health_attribute

InstancesHealthAttributes: TypeAlias = list[
    "capo_elastic_beanstalk.types.instances_health_attribute.InstancesHealthAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstancesHealthAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.instances_health_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.instances_health_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstancesHealthAttributes:
    import capo_elastic_beanstalk.types.instances_health_attribute

    out: InstancesHealthAttributes = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.instances_health_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: InstancesHealthAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.instances_health_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.instances_health_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstancesHealthAttributes:
    import capo_elastic_beanstalk.types.instances_health_attribute

    out: InstancesHealthAttributes = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.instances_health_attribute.deserialize_query(
                child
            )
        )
    return out
