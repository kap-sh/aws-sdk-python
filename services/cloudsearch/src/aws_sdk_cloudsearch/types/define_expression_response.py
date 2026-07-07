"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineExpressionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.expression_status


class DefineExpressionResponse(TypedDict, closed=True):
    expression: "aws_sdk_cloudsearch.types.expression_status.ExpressionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineExpressionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.expression_status

    aws_sdk_cloudsearch.types.expression_status.serialize_query(
        value["expression"], pairs, f"{prefix}.Expression"
    )


def deserialize_query(el: Element) -> DefineExpressionResponse:
    out: DefineExpressionResponse = {}  # type: ignore[typeddict-item]
    child_expression = el.find("Expression")
    if child_expression is not None:
        import aws_sdk_cloudsearch.types.expression_status

        out["expression"] = (
            aws_sdk_cloudsearch.types.expression_status.deserialize_query(
                child_expression
            )
        )
    else:
        raise DeserializationError("DefineExpressionResponse.expression required")
    return out
