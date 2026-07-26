"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssociatedTranscriptFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.associated_transcript_filter_name
    import capo_lex_models_v2.types.filter_values


class AssociatedTranscriptFilter(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.associated_transcript_filter_name.AssociatedTranscriptFilterName"
    """<p>The name of the field to use for filtering. The allowed names are IntentId and SlotTypeId.</p>"""
    values: "capo_lex_models_v2.types.filter_values.FilterValues"
    """<p>The values to use to filter the transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTranscriptFilter) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.associated_transcript_filter_name

    out["name"] = (
        capo_lex_models_v2.types.associated_transcript_filter_name.serialize_json(
            value["name"]
        )
    )
    import capo_lex_models_v2.types.filter_values

    out["values"] = capo_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> AssociatedTranscriptFilter:
    out: AssociatedTranscriptFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_lex_models_v2.types.associated_transcript_filter_name

        out["name"] = (
            capo_lex_models_v2.types.associated_transcript_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AssociatedTranscriptFilter.name required")
    if "values" in data:
        import capo_lex_models_v2.types.filter_values

        out["values"] = capo_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("AssociatedTranscriptFilter.values required")
    return out
