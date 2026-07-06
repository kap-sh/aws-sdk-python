"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineSuggesterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.suggester_status


class DefineSuggesterResponse(TypedDict, closed=True):
    suggester: "aws_sdk_cloudsearch.types.suggester_status.SuggesterStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineSuggesterResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.suggester_status

    aws_sdk_cloudsearch.types.suggester_status.serialize_query(
        value["suggester"], pairs, f"{prefix}.Suggester"
    )


def deserialize_query(el: Element) -> DefineSuggesterResponse:
    out: DefineSuggesterResponse = {}  # type: ignore[typeddict-item]
    child_suggester = el.find("Suggester")
    if child_suggester is not None:
        import aws_sdk_cloudsearch.types.suggester_status

        out["suggester"] = aws_sdk_cloudsearch.types.suggester_status.deserialize_query(
            child_suggester
        )
    else:
        raise DeserializationError("DefineSuggesterResponse.suggester required")
    return out
