"""Generated from Smithy shape ``com.amazonaws.opensearch#NaturalLanguageQueryGenerationOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.natural_language_query_generation_desired_state


class NaturalLanguageQueryGenerationOptionsInput(TypedDict, closed=True):
    desired_state: NotRequired[
        "capo_opensearch.types.natural_language_query_generation_desired_state.NaturalLanguageQueryGenerationDesiredState"
    ]
    """<p>The desired state of the natural language query generation feature. Valid values are ENABLED and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NaturalLanguageQueryGenerationOptionsInput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_opensearch.types.natural_language_query_generation_desired_state

        out["DesiredState"] = (
            capo_opensearch.types.natural_language_query_generation_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> NaturalLanguageQueryGenerationOptionsInput:
    out: NaturalLanguageQueryGenerationOptionsInput = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        import capo_opensearch.types.natural_language_query_generation_desired_state

        out["desired_state"] = (
            capo_opensearch.types.natural_language_query_generation_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    return out
