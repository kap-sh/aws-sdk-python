"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ExpressionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.expression
    import capo_cloudsearch.types.option_status


class ExpressionStatus(TypedDict, closed=True):
    options: "capo_cloudsearch.types.expression.Expression"
    """<p>The expression that is evaluated for sorting while processing a search request.</p>"""
    status: "capo_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: ExpressionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.expression

    capo_cloudsearch.types.expression.serialize_query(
        value["options"], pairs, f"{prefix}.Options"
    )
    import capo_cloudsearch.types.option_status

    capo_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> ExpressionStatus:
    out: ExpressionStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        import capo_cloudsearch.types.expression

        out["options"] = capo_cloudsearch.types.expression.deserialize_query(
            child_options
        )
    else:
        raise DeserializationError("ExpressionStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudsearch.types.option_status

        out["status"] = capo_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("ExpressionStatus.status required")
    return out
