"""Generated from Smithy shape ``com.amazonaws.cloudformation#DetectStackSetDriftOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.client_request_token


class DetectStackSetDriftOutput(TypedDict, closed=True):
    operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The ID of the drift detection StackSet operation.</p> <p>You can use this operation ID with <a>DescribeStackSetOperation</a> to monitor the progress of the drift detection operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetectStackSetDriftOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))


def deserialize_query(el: Element) -> DetectStackSetDriftOutput:
    out: DetectStackSetDriftOutput = {}  # type: ignore[typeddict-item]
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    return out
