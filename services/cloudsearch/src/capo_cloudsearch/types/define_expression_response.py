"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineExpressionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.expression_status


class DefineExpressionResponse(TypedDict, closed=True):
    expression: "capo_cloudsearch.types.expression_status.ExpressionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineExpressionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.expression_status

    capo_cloudsearch.types.expression_status.serialize_query(
        value["expression"], pairs, f"{key_prefix}Expression"
    )


def deserialize_query(el: Element) -> DefineExpressionResponse:
    out: DefineExpressionResponse = {}  # type: ignore[typeddict-item]
    child_expression = el.find("Expression")
    if child_expression is not None:
        import capo_cloudsearch.types.expression_status

        out["expression"] = capo_cloudsearch.types.expression_status.deserialize_query(
            child_expression
        )
    else:
        raise DeserializationError("DefineExpressionResponse.expression required")
    return out
