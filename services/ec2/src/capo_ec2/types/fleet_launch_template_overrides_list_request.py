"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateOverridesListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_launch_template_overrides_request

FleetLaunchTemplateOverridesListRequest: TypeAlias = list[
    "capo_ec2.types.fleet_launch_template_overrides_request.FleetLaunchTemplateOverridesRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateOverridesListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fleet_launch_template_overrides_request

        capo_ec2.types.fleet_launch_template_overrides_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateOverridesListRequest:
    import capo_ec2.types.fleet_launch_template_overrides_request

    out: FleetLaunchTemplateOverridesListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.fleet_launch_template_overrides_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FleetLaunchTemplateOverridesListRequest:
    import capo_ec2.types.fleet_launch_template_overrides_request

    out: FleetLaunchTemplateOverridesListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.fleet_launch_template_overrides_request.deserialize_ec2_query(
                child
            )
        )
    return out
