"""Generated from Smithy shape ``com.amazonaws.datazone#PredictionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.business_name_generation_configuration


class PredictionConfiguration(TypedDict, closed=True):
    business_name_generation: NotRequired[
        "capo_datazone.types.business_name_generation_configuration.BusinessNameGenerationConfiguration"
    ]
    """<p>The business name generation mechanism.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictionConfiguration) -> dict:
    out: dict = {}
    if "business_name_generation" in value:
        import capo_datazone.types.business_name_generation_configuration

        out["businessNameGeneration"] = (
            capo_datazone.types.business_name_generation_configuration.serialize_json(
                value["business_name_generation"]
            )
        )
    return out


def deserialize_json(data: dict) -> PredictionConfiguration:
    out: PredictionConfiguration = {}  # type: ignore[typeddict-item]
    if "businessNameGeneration" in data:
        import capo_datazone.types.business_name_generation_configuration

        out["business_name_generation"] = (
            capo_datazone.types.business_name_generation_configuration.deserialize_json(
                data["businessNameGeneration"]
            )
        )
    return out
