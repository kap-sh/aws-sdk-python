"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.sensitive_text


class UpdateRecommenderRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender to update.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The new description to assign to the recommender.</p>"""
    recommender_config: NotRequired[
        "capo_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The new configuration settings to apply to the recommender, including updated parameters and settings that define its behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "recommender_config" in value:
        import capo_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            capo_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommenderRequest:
    out: UpdateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RecommenderConfig" in data:
        import capo_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            capo_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    return out
