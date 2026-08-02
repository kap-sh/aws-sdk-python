"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBRecommendationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.recommended_action_update_list
    import capo_rds.types.string


class ModifyDBRecommendationMessage(TypedDict, closed=True):
    recommendation_id: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the recommendation to update.</p>"""
    locale: NotRequired["capo_rds.types.string.String"]
    """<p>The language of the modified recommendation.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The recommendation status to update.</p> <p>Valid values:</p> <ul> <li> <p>active</p> </li> <li> <p>dismissed</p> </li> </ul>"""
    recommended_action_updates: NotRequired[
        "capo_rds.types.recommended_action_update_list.RecommendedActionUpdateList"
    ]
    """<p>The list of recommended action status to update. You can update multiple recommended actions at one time.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBRecommendationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "recommendation_id" in value:
        pairs.append((f"{key_prefix}RecommendationId", str(value["recommendation_id"])))
    if "locale" in value:
        pairs.append((f"{key_prefix}Locale", str(value["locale"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "recommended_action_updates" in value:
        import capo_rds.types.recommended_action_update_list

        capo_rds.types.recommended_action_update_list.serialize_query(
            value["recommended_action_updates"],
            pairs,
            f"{key_prefix}RecommendedActionUpdates",
        )


def deserialize_query(el: Element) -> ModifyDBRecommendationMessage:
    out: ModifyDBRecommendationMessage = {}  # type: ignore[typeddict-item]
    child_recommendation_id = el.find("RecommendationId")
    if child_recommendation_id is not None:
        out["recommendation_id"] = str(child_recommendation_id.text or "")
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_recommended_action_updates = el.find("RecommendedActionUpdates")
    if child_recommended_action_updates is not None:
        import capo_rds.types.recommended_action_update_list

        out["recommended_action_updates"] = (
            capo_rds.types.recommended_action_update_list.deserialize_query(
                child_recommended_action_updates
            )
        )
    return out
