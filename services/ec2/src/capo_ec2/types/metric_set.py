"""Generated from Smithy shape ``com.amazonaws.ec2#MetricSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric

MetricSet: TypeAlias = list["capo_ec2.types.metric.Metric"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.metric

        capo_ec2.types.metric.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> MetricSet:
    import capo_ec2.types.metric

    out: MetricSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.metric.deserialize_ec2_query(child))
    return out
