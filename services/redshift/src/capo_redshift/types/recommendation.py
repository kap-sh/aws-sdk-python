"""Generated from Smithy shape ``com.amazonaws.redshift#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.impact_ranking_type
    import capo_redshift.types.recommended_action_list
    import capo_redshift.types.reference_link_list
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class Recommendation(TypedDict, closed=True):
    id: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier of the Advisor recommendation.</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster for which the recommendation is returned.</p>"""
    namespace_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Redshift cluster namespace ARN for which the recommendations is returned.</p>"""
    created_at: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The date and time (UTC) that the recommendation was created.</p>"""
    recommendation_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The type of Advisor recommendation.</p>"""
    title: NotRequired["capo_redshift.types.string.String"]
    """<p>The title of the recommendation.</p>"""
    description: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of the recommendation.</p>"""
    observation: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of what was observed about your cluster.</p>"""
    impact_ranking: NotRequired[
        "capo_redshift.types.impact_ranking_type.ImpactRankingType"
    ]
    """<p>The scale of the impact that the Advisor recommendation has to the performance and cost of the cluster.</p>"""
    recommendation_text: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of the recommendation.</p>"""
    recommended_actions: NotRequired[
        "capo_redshift.types.recommended_action_list.RecommendedActionList"
    ]
    """<p>List of Amazon Redshift recommended actions.</p>"""
    reference_links: NotRequired[
        "capo_redshift.types.reference_link_list.ReferenceLinkList"
    ]
    """<p>List of helpful links for more information about the Advisor recommendation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Recommendation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "namespace_arn" in value:
        pairs.append((f"{key_prefix}NamespaceArn", str(value["namespace_arn"])))
    if "created_at" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["created_at"], pairs, f"{key_prefix}CreatedAt"
        )
    if "recommendation_type" in value:
        pairs.append(
            (f"{key_prefix}RecommendationType", str(value["recommendation_type"]))
        )
    if "title" in value:
        pairs.append((f"{key_prefix}Title", str(value["title"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "observation" in value:
        pairs.append((f"{key_prefix}Observation", str(value["observation"])))
    if "impact_ranking" in value:
        import capo_redshift.types.impact_ranking_type

        capo_redshift.types.impact_ranking_type.serialize_query(
            value["impact_ranking"], pairs, f"{key_prefix}ImpactRanking"
        )
    if "recommendation_text" in value:
        pairs.append(
            (f"{key_prefix}RecommendationText", str(value["recommendation_text"]))
        )
    if "recommended_actions" in value:
        import capo_redshift.types.recommended_action_list

        capo_redshift.types.recommended_action_list.serialize_query(
            value["recommended_actions"], pairs, f"{key_prefix}RecommendedActions"
        )
    if "reference_links" in value:
        import capo_redshift.types.reference_link_list

        capo_redshift.types.reference_link_list.serialize_query(
            value["reference_links"], pairs, f"{key_prefix}ReferenceLinks"
        )


def deserialize_query(el: Element) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_namespace_arn = el.find("NamespaceArn")
    if child_namespace_arn is not None:
        out["namespace_arn"] = str(child_namespace_arn.text or "")
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_redshift.types.t_stamp

        out["created_at"] = capo_redshift.types.t_stamp.deserialize_query(
            child_created_at
        )
    child_recommendation_type = el.find("RecommendationType")
    if child_recommendation_type is not None:
        out["recommendation_type"] = str(child_recommendation_type.text or "")
    child_title = el.find("Title")
    if child_title is not None:
        out["title"] = str(child_title.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_observation = el.find("Observation")
    if child_observation is not None:
        out["observation"] = str(child_observation.text or "")
    child_impact_ranking = el.find("ImpactRanking")
    if child_impact_ranking is not None:
        import capo_redshift.types.impact_ranking_type

        out["impact_ranking"] = (
            capo_redshift.types.impact_ranking_type.deserialize_query(
                child_impact_ranking
            )
        )
    child_recommendation_text = el.find("RecommendationText")
    if child_recommendation_text is not None:
        out["recommendation_text"] = str(child_recommendation_text.text or "")
    child_recommended_actions = el.find("RecommendedActions")
    if child_recommended_actions is not None:
        import capo_redshift.types.recommended_action_list

        out["recommended_actions"] = (
            capo_redshift.types.recommended_action_list.deserialize_query(
                child_recommended_actions
            )
        )
    child_reference_links = el.find("ReferenceLinks")
    if child_reference_links is not None:
        import capo_redshift.types.reference_link_list

        out["reference_links"] = (
            capo_redshift.types.reference_link_list.deserialize_query(
                child_reference_links
            )
        )
    return out
