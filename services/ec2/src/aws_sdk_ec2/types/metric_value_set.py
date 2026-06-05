"""Generated from Smithy shape ``com.amazonaws.ec2#MetricValueSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_value

MetricValueSet: TypeAlias = list["aws_sdk_ec2.types.metric_value.MetricValue"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricValueSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.metric_value

        aws_sdk_ec2.types.metric_value.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> MetricValueSet:
    import aws_sdk_ec2.types.metric_value

    out: MetricValueSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.metric_value.deserialize_ec2_query(child))
    return out
