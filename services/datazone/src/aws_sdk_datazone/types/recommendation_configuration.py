"""Generated from Smithy shape ``com.amazonaws.datazone#RecommendationConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RecommendationConfiguration(TypedDict):
    enable_business_name_generation: NotRequired["bool"]
    """<p>Specifies whether automatic business name generation is to be enabled or not as part of the recommendation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationConfiguration) -> dict:
    out: dict = {}
    if "enable_business_name_generation" in value:
        out["enableBusinessNameGeneration"] = value["enable_business_name_generation"]
    return out


def deserialize_json(data: dict) -> RecommendationConfiguration:
    out: RecommendationConfiguration = {}  # type: ignore[typeddict-item]
    if "enableBusinessNameGeneration" in data:
        out["enable_business_name_generation"] = data["enableBusinessNameGeneration"]
    return out
