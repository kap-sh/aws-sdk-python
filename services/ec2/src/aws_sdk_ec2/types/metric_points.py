"""Generated from Smithy shape ``com.amazonaws.ec2#MetricPoints``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_point

MetricPoints: TypeAlias = list["aws_sdk_ec2.types.metric_point.MetricPoint"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricPoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.metric_point

        aws_sdk_ec2.types.metric_point.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> MetricPoints:
    import aws_sdk_ec2.types.metric_point

    out: MetricPoints = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.metric_point.deserialize_ec2_query(child))
    return out
