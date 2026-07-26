"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineSuggesterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.suggester_status


class DefineSuggesterResponse(TypedDict, closed=True):
    suggester: "capo_cloudsearch.types.suggester_status.SuggesterStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineSuggesterResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.suggester_status

    capo_cloudsearch.types.suggester_status.serialize_query(
        value["suggester"], pairs, f"{prefix}.Suggester"
    )


def deserialize_query(el: Element) -> DefineSuggesterResponse:
    out: DefineSuggesterResponse = {}  # type: ignore[typeddict-item]
    child_suggester = el.find("Suggester")
    if child_suggester is not None:
        import capo_cloudsearch.types.suggester_status

        out["suggester"] = capo_cloudsearch.types.suggester_status.deserialize_query(
            child_suggester
        )
    else:
        raise DeserializationError("DefineSuggesterResponse.suggester required")
    return out
