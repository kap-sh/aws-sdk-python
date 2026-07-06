"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides_list
    import aws_sdk_ec2.types.fleet_launch_template_specification


class FleetLaunchTemplateConfig(TypedDict, closed=True):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template.</p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_overrides_list.FleetLaunchTemplateOverridesList"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_specification" in value:
        import aws_sdk_ec2.types.fleet_launch_template_specification

        aws_sdk_ec2.types.fleet_launch_template_specification.serialize_ec2_query(
            value["launch_template_specification"],
            pairs,
            f"{prefix}.LaunchTemplateSpecification",
        )
    if "overrides" in value:
        import aws_sdk_ec2.types.fleet_launch_template_overrides_list

        aws_sdk_ec2.types.fleet_launch_template_overrides_list.serialize_ec2_query(
            value["overrides"], pairs, f"{prefix}.Overrides"
        )


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateConfig:
    out: FleetLaunchTemplateConfig = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("LaunchTemplateSpecification")
    if child_launch_template_specification is not None:
        import aws_sdk_ec2.types.fleet_launch_template_specification

        out["launch_template_specification"] = (
            aws_sdk_ec2.types.fleet_launch_template_specification.deserialize_ec2_query(
                child_launch_template_specification
            )
        )
    if el.find("Overrides") is not None:
        import aws_sdk_ec2.types.fleet_launch_template_overrides_list

        out["overrides"] = (
            aws_sdk_ec2.types.fleet_launch_template_overrides_list.deserialize_ec2_query(
                el, "Overrides"
            )
        )
    return out
