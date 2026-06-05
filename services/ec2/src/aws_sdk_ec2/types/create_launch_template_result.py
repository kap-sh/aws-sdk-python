"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template
    import aws_sdk_ec2.types.validation_warning


class CreateLaunchTemplateResult(TypedDict):
    launch_template: NotRequired["aws_sdk_ec2.types.launch_template.LaunchTemplate"]
    """<p>Information about the launch template.</p>"""
    warning: NotRequired["aws_sdk_ec2.types.validation_warning.ValidationWarning"]
    """<p>If the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue that's found.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLaunchTemplateResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template" in value:
        import aws_sdk_ec2.types.launch_template

        aws_sdk_ec2.types.launch_template.serialize_ec2_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )
    if "warning" in value:
        import aws_sdk_ec2.types.validation_warning

        aws_sdk_ec2.types.validation_warning.serialize_ec2_query(
            value["warning"], pairs, f"{prefix}.Warning"
        )


def deserialize_ec2_query(el: Element) -> CreateLaunchTemplateResult:
    out: CreateLaunchTemplateResult = {}  # type: ignore[typeddict-item]
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import aws_sdk_ec2.types.launch_template

        out["launch_template"] = (
            aws_sdk_ec2.types.launch_template.deserialize_ec2_query(
                child_launch_template
            )
        )
    child_warning = el.find("Warning")
    if child_warning is not None:
        import aws_sdk_ec2.types.validation_warning

        out["warning"] = aws_sdk_ec2.types.validation_warning.deserialize_ec2_query(
            child_warning
        )
    return out
