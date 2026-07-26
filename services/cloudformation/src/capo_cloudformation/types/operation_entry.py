"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.operation_id
    import capo_cloudformation.types.operation_type


class OperationEntry(TypedDict, closed=True):
    operation_type: NotRequired[
        "capo_cloudformation.types.operation_type.OperationType"
    ]
    """<p>The type of operation.</p>"""
    operation_id: NotRequired["capo_cloudformation.types.operation_id.OperationId"]
    """<p>The unique identifier for the operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "operation_type" in value:
        import capo_cloudformation.types.operation_type

        capo_cloudformation.types.operation_type.serialize_query(
            value["operation_type"], pairs, f"{prefix}.OperationType"
        )
    if "operation_id" in value:
        pairs.append((f"{prefix}.OperationId", str(value["operation_id"])))


def deserialize_query(el: Element) -> OperationEntry:
    out: OperationEntry = {}  # type: ignore[typeddict-item]
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import capo_cloudformation.types.operation_type

        out["operation_type"] = (
            capo_cloudformation.types.operation_type.deserialize_query(
                child_operation_type
            )
        )
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    return out
