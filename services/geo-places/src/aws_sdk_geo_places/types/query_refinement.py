"""Generated from Smithy shape ``com.amazonaws.geoplaces#QueryRefinement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.sensitive_string


class QueryRefinement(TypedDict, closed=True):
    refined_term: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The term that will be suggested to the user.</p>"""
    original_term: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The sub-string of the original query that is replaced by this query term.</p>"""
    start_index: "int"
    """<p>Start index of the parsed component.</p>"""
    end_index: "int"
    """<p>End index of the parsed query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryRefinement) -> dict:
    out: dict = {}
    out["RefinedTerm"] = value["refined_term"]
    out["OriginalTerm"] = value["original_term"]
    out["StartIndex"] = value["start_index"]
    out["EndIndex"] = value["end_index"]
    return out


def deserialize_json(data: dict) -> QueryRefinement:
    out: QueryRefinement = {}  # type: ignore[typeddict-item]
    if "RefinedTerm" in data:
        out["refined_term"] = data["RefinedTerm"]
    else:
        raise DeserializationError("QueryRefinement.refined_term required")
    if "OriginalTerm" in data:
        out["original_term"] = data["OriginalTerm"]
    else:
        raise DeserializationError("QueryRefinement.original_term required")
    if "StartIndex" in data:
        out["start_index"] = data["StartIndex"]
    else:
        raise DeserializationError("QueryRefinement.start_index required")
    if "EndIndex" in data:
        out["end_index"] = data["EndIndex"]
    else:
        raise DeserializationError("QueryRefinement.end_index required")
    return out
