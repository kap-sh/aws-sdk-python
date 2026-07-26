"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryItemAdditionalAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.match_rationale


class GlossaryItemAdditionalAttributes(TypedDict, closed=True):
    match_rationale: NotRequired["capo_datazone.types.match_rationale.MatchRationale"]
    """<p>List of rationales indicating why this item was matched by search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryItemAdditionalAttributes) -> dict:
    out: dict = {}
    if "match_rationale" in value:
        import capo_datazone.types.match_rationale

        out["matchRationale"] = capo_datazone.types.match_rationale.serialize_json(
            value["match_rationale"]
        )
    return out


def deserialize_json(data: dict) -> GlossaryItemAdditionalAttributes:
    out: GlossaryItemAdditionalAttributes = {}  # type: ignore[typeddict-item]
    if "matchRationale" in data:
        import capo_datazone.types.match_rationale

        out["match_rationale"] = capo_datazone.types.match_rationale.deserialize_json(
            data["matchRationale"]
        )
    return out
