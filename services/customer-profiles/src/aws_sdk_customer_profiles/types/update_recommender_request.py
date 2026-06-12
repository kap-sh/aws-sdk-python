"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateRecommenderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_config
    import aws_sdk_customer_profiles.types.sensitive_text


class UpdateRecommenderRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender to update.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The new description to assign to the recommender.</p>"""
    recommender_config: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The new configuration settings to apply to the recommender, including updated parameters and settings that define its behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "recommender_config" in value:
        import aws_sdk_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            aws_sdk_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommenderRequest:
    out: UpdateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RecommenderConfig" in data:
        import aws_sdk_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            aws_sdk_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    return out
