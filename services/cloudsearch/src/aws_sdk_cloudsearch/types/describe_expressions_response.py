"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeExpressionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.expression_status_list


class DescribeExpressionsResponse(TypedDict):
    expressions: "aws_sdk_cloudsearch.types.expression_status_list.ExpressionStatusList"
    """<p>The expressions configured for the domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeExpressionsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.expression_status_list

    aws_sdk_cloudsearch.types.expression_status_list.serialize_query(
        value["expressions"], pairs, f"{prefix}.Expressions"
    )


def deserialize_query(el: Element) -> DescribeExpressionsResponse:
    out: DescribeExpressionsResponse = {}  # type: ignore[typeddict-item]
    child_expressions = el.find("Expressions")
    if child_expressions is not None:
        import aws_sdk_cloudsearch.types.expression_status_list

        out["expressions"] = (
            aws_sdk_cloudsearch.types.expression_status_list.deserialize_query(
                child_expressions
            )
        )
    else:
        raise DeserializationError("DescribeExpressionsResponse.expressions required")
    return out
