"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_specification
    import aws_sdk_ec2.types.launch_template_overrides_list


class LaunchTemplateConfig(TypedDict):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template to use. Make sure that the launch template does not contain the <code>NetworkInterfaceId</code> parameter because you can't specify a network interface ID in a Spot Fleet.</p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.launch_template_overrides_list.LaunchTemplateOverridesList"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_specification" in value:
        import aws_sdk_ec2.types.fleet_launch_template_specification

        aws_sdk_ec2.types.fleet_launch_template_specification.serialize_ec2_query(
            value["launch_template_specification"],
            pairs,
            f"{prefix}.LaunchTemplateSpecification",
        )
    if "overrides" in value:
        import aws_sdk_ec2.types.launch_template_overrides_list

        aws_sdk_ec2.types.launch_template_overrides_list.serialize_ec2_query(
            value["overrides"], pairs, f"{prefix}.Overrides"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateConfig:
    out: LaunchTemplateConfig = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("LaunchTemplateSpecification")
    if child_launch_template_specification is not None:
        import aws_sdk_ec2.types.fleet_launch_template_specification

        out["launch_template_specification"] = (
            aws_sdk_ec2.types.fleet_launch_template_specification.deserialize_ec2_query(
                child_launch_template_specification
            )
        )
    if el.find("Overrides") is not None:
        import aws_sdk_ec2.types.launch_template_overrides_list

        out["overrides"] = (
            aws_sdk_ec2.types.launch_template_overrides_list.deserialize_ec2_query(
                el, "Overrides"
            )
        )
    return out
