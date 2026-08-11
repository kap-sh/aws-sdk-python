"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_launch_template_overrides

FleetLaunchTemplateOverridesList: TypeAlias = list[
    "capo_ec2.types.fleet_launch_template_overrides.FleetLaunchTemplateOverrides"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateOverridesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fleet_launch_template_overrides

        capo_ec2.types.fleet_launch_template_overrides.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateOverridesList:
    import capo_ec2.types.fleet_launch_template_overrides

    out: FleetLaunchTemplateOverridesList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.fleet_launch_template_overrides.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FleetLaunchTemplateOverridesList:
    import capo_ec2.types.fleet_launch_template_overrides

    out: FleetLaunchTemplateOverridesList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.fleet_launch_template_overrides.deserialize_ec2_query(child)
        )
    return out
