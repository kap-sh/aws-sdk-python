"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackDriftDetectionStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_drift_detection_id


class DescribeStackDriftDetectionStatusInput(TypedDict):
    stack_drift_detection_id: NotRequired[
        "aws_sdk_cloudformation.types.stack_drift_detection_id.StackDriftDetectionId"
    ]
    """<p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results CloudFormation retains for any given stack, and for how long, may vary.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackDriftDetectionStatusInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "stack_drift_detection_id" in value:
        pairs.append(
            (f"{prefix}.StackDriftDetectionId", str(value["stack_drift_detection_id"]))
        )


def deserialize_query(el: Element) -> DescribeStackDriftDetectionStatusInput:
    out: DescribeStackDriftDetectionStatusInput = {}  # type: ignore[typeddict-item]
    child_stack_drift_detection_id = el.find("StackDriftDetectionId")
    if child_stack_drift_detection_id is not None:
        out["stack_drift_detection_id"] = str(child_stack_drift_detection_id.text or "")
    return out
