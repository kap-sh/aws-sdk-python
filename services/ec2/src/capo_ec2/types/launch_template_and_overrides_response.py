"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateAndOverridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_launch_template_overrides
    import capo_ec2.types.fleet_launch_template_specification


class LaunchTemplateAndOverridesResponse(TypedDict, closed=True):
    launch_template_specification: NotRequired[
        "capo_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template.</p>"""
    overrides: NotRequired[
        "capo_ec2.types.fleet_launch_template_overrides.FleetLaunchTemplateOverrides"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateAndOverridesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_specification" in value:
        import capo_ec2.types.fleet_launch_template_specification

        capo_ec2.types.fleet_launch_template_specification.serialize_ec2_query(
            value["launch_template_specification"],
            pairs,
            f"{key_prefix}LaunchTemplateSpecification",
        )
    if "overrides" in value:
        import capo_ec2.types.fleet_launch_template_overrides

        capo_ec2.types.fleet_launch_template_overrides.serialize_ec2_query(
            value["overrides"], pairs, f"{key_prefix}Overrides"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateAndOverridesResponse:
    out: LaunchTemplateAndOverridesResponse = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("launchTemplateSpecification")
    if child_launch_template_specification is not None:
        import capo_ec2.types.fleet_launch_template_specification

        out["launch_template_specification"] = (
            capo_ec2.types.fleet_launch_template_specification.deserialize_ec2_query(
                child_launch_template_specification
            )
        )
    child_overrides = el.find("overrides")
    if child_overrides is not None:
        import capo_ec2.types.fleet_launch_template_overrides

        out["overrides"] = (
            capo_ec2.types.fleet_launch_template_overrides.deserialize_ec2_query(
                child_overrides
            )
        )
    return out
