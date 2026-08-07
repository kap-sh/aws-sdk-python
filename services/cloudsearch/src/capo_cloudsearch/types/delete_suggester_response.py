"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteSuggesterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.suggester_status


class DeleteSuggesterResponse(TypedDict, closed=True):
    suggester: "capo_cloudsearch.types.suggester_status.SuggesterStatus"
    """<p>The status of the suggester being deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSuggesterResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.suggester_status

    capo_cloudsearch.types.suggester_status.serialize_query(
        value["suggester"], pairs, f"{key_prefix}Suggester"
    )


def deserialize_query(el: Element) -> DeleteSuggesterResponse:
    out: DeleteSuggesterResponse = {}  # type: ignore[typeddict-item]
    child_suggester = el.find("Suggester")
    if child_suggester is not None:
        import capo_cloudsearch.types.suggester_status

        out["suggester"] = capo_cloudsearch.types.suggester_status.deserialize_query(
            child_suggester
        )
    else:
        raise DeserializationError("DeleteSuggesterResponse.suggester required")
    return out
