"""Generated from Smithy shape ``com.amazonaws.redshift#SupportedOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class SupportedOperation(TypedDict, closed=True):
    operation_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A list of the supported operations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedOperation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "operation_name" in value:
        pairs.append((f"{prefix}.OperationName", str(value["operation_name"])))


def deserialize_query(el: Element) -> SupportedOperation:
    out: SupportedOperation = {}  # type: ignore[typeddict-item]
    child_operation_name = el.find("OperationName")
    if child_operation_name is not None:
        out["operation_name"] = str(child_operation_name.text or "")
    return out
