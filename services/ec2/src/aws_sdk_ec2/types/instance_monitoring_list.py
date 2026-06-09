"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMonitoringList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_monitoring

InstanceMonitoringList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_monitoring.InstanceMonitoring"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceMonitoringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_monitoring

        aws_sdk_ec2.types.instance_monitoring.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceMonitoringList:
    import aws_sdk_ec2.types.instance_monitoring

    out: InstanceMonitoringList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_monitoring.deserialize_ec2_query(child))
    return out
