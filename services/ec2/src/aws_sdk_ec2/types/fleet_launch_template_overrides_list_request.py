"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateOverridesListRequest``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides_request

FleetLaunchTemplateOverridesListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_launch_template_overrides_request.FleetLaunchTemplateOverridesRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateOverridesListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fleet_launch_template_overrides_request

        aws_sdk_ec2.types.fleet_launch_template_overrides_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> FleetLaunchTemplateOverridesListRequest:
    import aws_sdk_ec2.types.fleet_launch_template_overrides_request

    out: FleetLaunchTemplateOverridesListRequest = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.fleet_launch_template_overrides_request.deserialize_ec2_query(
                child
            )
        )
    return out
