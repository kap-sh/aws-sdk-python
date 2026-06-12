"""Generated from Smithy shape ``com.amazonaws.redshift#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.impact_ranking_type
    import aws_sdk_redshift.types.recommended_action_list
    import aws_sdk_redshift.types.reference_link_list
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class Recommendation(TypedDict):
    id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier of the Advisor recommendation.</p>"""
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of the cluster for which the recommendation is returned.</p>"""
    namespace_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Redshift cluster namespace ARN for which the recommendations is returned.</p>"""
    created_at: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date and time (UTC) that the recommendation was created.</p>"""
    recommendation_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The type of Advisor recommendation.</p>"""
    title: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The title of the recommendation.</p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of the recommendation.</p>"""
    observation: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of what was observed about your cluster.</p>"""
    impact_ranking: NotRequired[
        "aws_sdk_redshift.types.impact_ranking_type.ImpactRankingType"
    ]
    """<p>The scale of the impact that the Advisor recommendation has to the performance and cost of the cluster.</p>"""
    recommendation_text: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of the recommendation.</p>"""
    recommended_actions: NotRequired[
        "aws_sdk_redshift.types.recommended_action_list.RecommendedActionList"
    ]
    """<p>List of Amazon Redshift recommended actions.</p>"""
    reference_links: NotRequired[
        "aws_sdk_redshift.types.reference_link_list.ReferenceLinkList"
    ]
    """<p>List of helpful links for more information about the Advisor recommendation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Recommendation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "namespace_arn" in value:
        pairs.append((f"{prefix}.NamespaceArn", str(value["namespace_arn"])))
    if "created_at" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["created_at"], pairs, f"{prefix}.CreatedAt"
        )
    if "recommendation_type" in value:
        pairs.append(
            (f"{prefix}.RecommendationType", str(value["recommendation_type"]))
        )
    if "title" in value:
        pairs.append((f"{prefix}.Title", str(value["title"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "observation" in value:
        pairs.append((f"{prefix}.Observation", str(value["observation"])))
    if "impact_ranking" in value:
        import aws_sdk_redshift.types.impact_ranking_type

        aws_sdk_redshift.types.impact_ranking_type.serialize_query(
            value["impact_ranking"], pairs, f"{prefix}.ImpactRanking"
        )
    if "recommendation_text" in value:
        pairs.append(
            (f"{prefix}.RecommendationText", str(value["recommendation_text"]))
        )
    if "recommended_actions" in value:
        import aws_sdk_redshift.types.recommended_action_list

        aws_sdk_redshift.types.recommended_action_list.serialize_query(
            value["recommended_actions"], pairs, f"{prefix}.RecommendedActions"
        )
    if "reference_links" in value:
        import aws_sdk_redshift.types.reference_link_list

        aws_sdk_redshift.types.reference_link_list.serialize_query(
            value["reference_links"], pairs, f"{prefix}.ReferenceLinks"
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
        import aws_sdk_redshift.types.t_stamp

        out["created_at"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
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
        import aws_sdk_redshift.types.impact_ranking_type

        out["impact_ranking"] = (
            aws_sdk_redshift.types.impact_ranking_type.deserialize_query(
                child_impact_ranking
            )
        )
    child_recommendation_text = el.find("RecommendationText")
    if child_recommendation_text is not None:
        out["recommendation_text"] = str(child_recommendation_text.text or "")
    child_recommended_actions = el.find("RecommendedActions")
    if child_recommended_actions is not None:
        import aws_sdk_redshift.types.recommended_action_list

        out["recommended_actions"] = (
            aws_sdk_redshift.types.recommended_action_list.deserialize_query(
                child_recommended_actions
            )
        )
    child_reference_links = el.find("ReferenceLinks")
    if child_reference_links is not None:
        import aws_sdk_redshift.types.reference_link_list

        out["reference_links"] = (
            aws_sdk_redshift.types.reference_link_list.deserialize_query(
                child_reference_links
            )
        )
    return out
