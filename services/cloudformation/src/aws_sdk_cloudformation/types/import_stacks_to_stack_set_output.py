"""Generated from Smithy shape ``com.amazonaws.cloudformation#ImportStacksToStackSetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.client_request_token


class ImportStacksToStackSetOutput(TypedDict):
    operation_id: NotRequired[
        "aws_sdk_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the StackSet operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ImportStacksToStackSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "operation_id" in value:
        pairs.append((f"{prefix}.OperationId", str(value["operation_id"])))


def deserialize_query(el: Element) -> ImportStacksToStackSetOutput:
    out: ImportStacksToStackSetOutput = {}  # type: ignore[typeddict-item]
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    return out
