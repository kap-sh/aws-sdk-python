"""Generated from Smithy shape ``com.amazonaws.cloudformation#DetectStackResourceDriftOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_resource_drift


class DetectStackResourceDriftOutput(TypedDict, closed=True):
    stack_resource_drift: NotRequired[
        "capo_cloudformation.types.stack_resource_drift.StackResourceDrift"
    ]
    """<p>Information about whether the resource's actual configuration has drifted from its expected template configuration, including actual and expected property values and any differences detected.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetectStackResourceDriftOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_resource_drift" in value:
        import capo_cloudformation.types.stack_resource_drift

        capo_cloudformation.types.stack_resource_drift.serialize_query(
            value["stack_resource_drift"], pairs, f"{prefix}.StackResourceDrift"
        )


def deserialize_query(el: Element) -> DetectStackResourceDriftOutput:
    out: DetectStackResourceDriftOutput = {}  # type: ignore[typeddict-item]
    child_stack_resource_drift = el.find("StackResourceDrift")
    if child_stack_resource_drift is not None:
        import capo_cloudformation.types.stack_resource_drift

        out["stack_resource_drift"] = (
            capo_cloudformation.types.stack_resource_drift.deserialize_query(
                child_stack_resource_drift
            )
        )
    return out
