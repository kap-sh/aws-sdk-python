"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.overrides


class LaunchTemplate(TypedDict, closed=True):
    launch_template_specification: NotRequired[
        "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The launch template.</p>"""
    overrides: NotRequired["capo_auto_scaling.types.overrides.Overrides"]
    """<p>Any properties that you specify override the same properties in the launch template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchTemplate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_specification" in value:
        import capo_auto_scaling.types.launch_template_specification

        capo_auto_scaling.types.launch_template_specification.serialize_query(
            value["launch_template_specification"],
            pairs,
            f"{prefix}.LaunchTemplateSpecification",
        )
    if "overrides" in value:
        import capo_auto_scaling.types.overrides

        capo_auto_scaling.types.overrides.serialize_query(
            value["overrides"], pairs, f"{prefix}.Overrides"
        )


def deserialize_query(el: Element) -> LaunchTemplate:
    out: LaunchTemplate = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("LaunchTemplateSpecification")
    if child_launch_template_specification is not None:
        import capo_auto_scaling.types.launch_template_specification

        out["launch_template_specification"] = (
            capo_auto_scaling.types.launch_template_specification.deserialize_query(
                child_launch_template_specification
            )
        )
    child_overrides = el.find("Overrides")
    if child_overrides is not None:
        import capo_auto_scaling.types.overrides

        out["overrides"] = capo_auto_scaling.types.overrides.deserialize_query(
            child_overrides
        )
    return out
