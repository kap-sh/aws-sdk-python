"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteExpressionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.standard_name


class DeleteExpressionRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    expression_name: "aws_sdk_cloudsearch.types.standard_name.StandardName"
    """<p>The name of the <code><a>Expression</a></code> to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteExpressionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    pairs.append((f"{prefix}.ExpressionName", str(value["expression_name"])))


def deserialize_query(el: Element) -> DeleteExpressionRequest:
    out: DeleteExpressionRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DeleteExpressionRequest.domain_name required")
    child_expression_name = el.find("ExpressionName")
    if child_expression_name is not None:
        out["expression_name"] = str(child_expression_name.text or "")
    else:
        raise DeserializationError("DeleteExpressionRequest.expression_name required")
    return out
