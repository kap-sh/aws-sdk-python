"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineExpressionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.expression


class DefineExpressionRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    expression: "aws_sdk_cloudsearch.types.expression.Expression"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineExpressionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    import aws_sdk_cloudsearch.types.expression

    aws_sdk_cloudsearch.types.expression.serialize_query(
        value["expression"], pairs, f"{prefix}.Expression"
    )


def deserialize_query(el: Element) -> DefineExpressionRequest:
    out: DefineExpressionRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DefineExpressionRequest.domain_name required")
    child_expression = el.find("Expression")
    if child_expression is not None:
        import aws_sdk_cloudsearch.types.expression

        out["expression"] = aws_sdk_cloudsearch.types.expression.deserialize_query(
            child_expression
        )
    else:
        raise DeserializationError("DefineExpressionRequest.expression required")
    return out
