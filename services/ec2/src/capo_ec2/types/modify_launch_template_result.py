"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyLaunchTemplateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template


class ModifyLaunchTemplateResult(TypedDict, closed=True):
    launch_template: NotRequired["capo_ec2.types.launch_template.LaunchTemplate"]
    """<p>Information about the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyLaunchTemplateResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template" in value:
        import capo_ec2.types.launch_template

        capo_ec2.types.launch_template.serialize_ec2_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )


def deserialize_ec2_query(el: Element) -> ModifyLaunchTemplateResult:
    out: ModifyLaunchTemplateResult = {}  # type: ignore[typeddict-item]
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_ec2.types.launch_template

        out["launch_template"] = capo_ec2.types.launch_template.deserialize_ec2_query(
            child_launch_template
        )
    return out
