"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteSuggesterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.suggester_status


class DeleteSuggesterResponse(TypedDict):
    suggester: "aws_sdk_cloudsearch.types.suggester_status.SuggesterStatus"
    """<p>The status of the suggester being deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSuggesterResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.suggester_status

    aws_sdk_cloudsearch.types.suggester_status.serialize_query(
        value["suggester"], pairs, f"{prefix}.Suggester"
    )


def deserialize_query(el: Element) -> DeleteSuggesterResponse:
    out: DeleteSuggesterResponse = {}  # type: ignore[typeddict-item]
    child_suggester = el.find("Suggester")
    if child_suggester is not None:
        import aws_sdk_cloudsearch.types.suggester_status

        out["suggester"] = aws_sdk_cloudsearch.types.suggester_status.deserialize_query(
            child_suggester
        )
    else:
        raise DeserializationError("DeleteSuggesterResponse.suggester required")
    return out
