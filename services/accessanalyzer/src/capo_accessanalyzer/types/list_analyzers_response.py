"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAnalyzersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzers_list
    import capo_accessanalyzer.types.token


class ListAnalyzersResponse(TypedDict, closed=True):
    analyzers: "capo_accessanalyzer.types.analyzers_list.AnalyzersList"
    """<p>The analyzers retrieved.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyzersResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.analyzers_list

    out["analyzers"] = capo_accessanalyzer.types.analyzers_list.serialize_json(
        value["analyzers"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnalyzersResponse:
    out: ListAnalyzersResponse = {}  # type: ignore[typeddict-item]
    if "analyzers" in data:
        import capo_accessanalyzer.types.analyzers_list

        out["analyzers"] = capo_accessanalyzer.types.analyzers_list.deserialize_json(
            data["analyzers"]
        )
    else:
        raise DeserializationError("ListAnalyzersResponse.analyzers required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
