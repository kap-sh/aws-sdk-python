"""Generated from Smithy shape ``com.amazonaws.cloudsearch#Expression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.expression_value
    import aws_sdk_cloudsearch.types.standard_name


class Expression(TypedDict):
    expression_name: "aws_sdk_cloudsearch.types.standard_name.StandardName"
    expression_value: "aws_sdk_cloudsearch.types.expression_value.ExpressionValue"


# --- awsQuery ser/de ---
def serialize_query(
    value: Expression, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ExpressionName", str(value["expression_name"])))
    pairs.append((f"{prefix}.ExpressionValue", str(value["expression_value"])))


def deserialize_query(el: Element) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    child_expression_name = el.find("ExpressionName")
    if child_expression_name is not None:
        out["expression_name"] = str(child_expression_name.text or "")
    else:
        raise DeserializationError("Expression.expression_name required")
    child_expression_value = el.find("ExpressionValue")
    if child_expression_value is not None:
        out["expression_value"] = str(child_expression_value.text or "")
    else:
        raise DeserializationError("Expression.expression_value required")
    return out
