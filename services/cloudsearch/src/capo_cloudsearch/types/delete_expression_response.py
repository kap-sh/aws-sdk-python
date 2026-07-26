"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteExpressionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.expression_status


class DeleteExpressionResponse(TypedDict, closed=True):
    expression: "capo_cloudsearch.types.expression_status.ExpressionStatus"
    """<p>The status of the expression being deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteExpressionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.expression_status

    capo_cloudsearch.types.expression_status.serialize_query(
        value["expression"], pairs, f"{prefix}.Expression"
    )


def deserialize_query(el: Element) -> DeleteExpressionResponse:
    out: DeleteExpressionResponse = {}  # type: ignore[typeddict-item]
    child_expression = el.find("Expression")
    if child_expression is not None:
        import capo_cloudsearch.types.expression_status

        out["expression"] = capo_cloudsearch.types.expression_status.deserialize_query(
            child_expression
        )
    else:
        raise DeserializationError("DeleteExpressionResponse.expression required")
    return out
