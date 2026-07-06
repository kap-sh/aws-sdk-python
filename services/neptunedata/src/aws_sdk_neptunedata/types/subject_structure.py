"""Generated from Smithy shape ``com.amazonaws.neptunedata#SubjectStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.predicates


class SubjectStructure(TypedDict, closed=True):
    count: NotRequired["int"]
    """<p>Number of occurrences of this specific structure.</p>"""
    predicates: NotRequired["aws_sdk_neptunedata.types.predicates.Predicates"]
    """<p>A list of predicates present in this specific structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectStructure) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "predicates" in value:
        import aws_sdk_neptunedata.types.predicates

        out["predicates"] = aws_sdk_neptunedata.types.predicates.serialize_json(
            value["predicates"]
        )
    return out


def deserialize_json(data: dict) -> SubjectStructure:
    out: SubjectStructure = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "predicates" in data:
        import aws_sdk_neptunedata.types.predicates

        out["predicates"] = aws_sdk_neptunedata.types.predicates.deserialize_json(
            data["predicates"]
        )
    return out
