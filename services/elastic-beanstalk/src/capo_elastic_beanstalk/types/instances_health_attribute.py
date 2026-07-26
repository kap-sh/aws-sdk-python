"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#InstancesHealthAttribute``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

InstancesHealthAttribute: TypeAlias = Literal[
    "HealthStatus",
    "Color",
    "Causes",
    "ApplicationMetrics",
    "RefreshedAt",
    "LaunchedAt",
    "System",
    "Deployment",
    "AvailabilityZone",
    "InstanceType",
    "All",
]


# --- awsQuery ser/de ---
def to_query_text(value: InstancesHealthAttribute) -> str:
    return value


def from_query_text(text: str) -> InstancesHealthAttribute:
    return cast(InstancesHealthAttribute, text)


def serialize_query(
    value: InstancesHealthAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InstancesHealthAttribute:
    return from_query_text(el.text or "")
