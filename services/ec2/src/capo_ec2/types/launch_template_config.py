"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_launch_template_specification
    import capo_ec2.types.launch_template_overrides_list


class LaunchTemplateConfig(TypedDict, closed=True):
    launch_template_specification: NotRequired[
        "capo_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template to use. Make sure that the launch template does not contain the <code>NetworkInterfaceId</code> parameter because you can't specify a network interface ID in a Spot Fleet.</p>"""
    overrides: NotRequired[
        "capo_ec2.types.launch_template_overrides_list.LaunchTemplateOverridesList"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateConfig, pairs: list[tuple[str, str]], prefix: str
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
        import capo_ec2.types.launch_template_overrides_list

        capo_ec2.types.launch_template_overrides_list.serialize_ec2_query(
            value["overrides"], pairs, f"{key_prefix}Overrides"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateConfig:
    out: LaunchTemplateConfig = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("launchTemplateSpecification")
    if child_launch_template_specification is not None:
        import capo_ec2.types.fleet_launch_template_specification

        out["launch_template_specification"] = (
            capo_ec2.types.fleet_launch_template_specification.deserialize_ec2_query(
                child_launch_template_specification
            )
        )
    if el.find("overrides") is not None:
        import capo_ec2.types.launch_template_overrides_list

        out["overrides"] = (
            capo_ec2.types.launch_template_overrides_list.deserialize_ec2_query(
                el, "overrides"
            )
        )
    return out
