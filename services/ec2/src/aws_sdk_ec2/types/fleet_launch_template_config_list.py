"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_config

FleetLaunchTemplateConfigList: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_launch_template_config.FleetLaunchTemplateConfig"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateConfigList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fleet_launch_template_config

        aws_sdk_ec2.types.fleet_launch_template_config.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> FleetLaunchTemplateConfigList:
    import aws_sdk_ec2.types.fleet_launch_template_config

    out: FleetLaunchTemplateConfigList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.fleet_launch_template_config.deserialize_ec2_query(child)
        )
    return out
