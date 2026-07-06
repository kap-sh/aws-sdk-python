"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateAndOverridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides
    import aws_sdk_ec2.types.fleet_launch_template_specification


class LaunchTemplateAndOverridesResponse(TypedDict, closed=True):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template.</p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_overrides.FleetLaunchTemplateOverrides"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateAndOverridesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_specification" in value:
        import aws_sdk_ec2.types.fleet_launch_template_specification

        aws_sdk_ec2.types.fleet_launch_template_specification.serialize_ec2_query(
            value["launch_template_specification"],
            pairs,
            f"{prefix}.LaunchTemplateSpecification",
        )
    if "overrides" in value:
        import aws_sdk_ec2.types.fleet_launch_template_overrides

        aws_sdk_ec2.types.fleet_launch_template_overrides.serialize_ec2_query(
            value["overrides"], pairs, f"{prefix}.Overrides"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateAndOverridesResponse:
    out: LaunchTemplateAndOverridesResponse = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("LaunchTemplateSpecification")
    if child_launch_template_specification is not None:
        import aws_sdk_ec2.types.fleet_launch_template_specification

        out["launch_template_specification"] = (
            aws_sdk_ec2.types.fleet_launch_template_specification.deserialize_ec2_query(
                child_launch_template_specification
            )
        )
    child_overrides = el.find("Overrides")
    if child_overrides is not None:
        import aws_sdk_ec2.types.fleet_launch_template_overrides

        out["overrides"] = (
            aws_sdk_ec2.types.fleet_launch_template_overrides.deserialize_ec2_query(
                child_overrides
            )
        )
    return out
