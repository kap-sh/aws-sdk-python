"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_config_request

FleetLaunchTemplateConfigListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_launch_template_config_request.FleetLaunchTemplateConfigRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateConfigListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fleet_launch_template_config_request

        aws_sdk_ec2.types.fleet_launch_template_config_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> FleetLaunchTemplateConfigListRequest:
    import aws_sdk_ec2.types.fleet_launch_template_config_request

    out: FleetLaunchTemplateConfigListRequest = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.fleet_launch_template_config_request.deserialize_ec2_query(
                child
            )
        )
    return out
