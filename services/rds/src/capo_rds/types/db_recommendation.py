"""Generated from Smithy shape ``com.amazonaws.rds#DBRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.doc_link_list
    import capo_rds.types.issue_details
    import capo_rds.types.recommended_action_list
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class DBRecommendation(TypedDict, closed=True):
    recommendation_id: NotRequired["capo_rds.types.string.String"]
    """<p>The unique identifier of the recommendation.</p>"""
    type_id: NotRequired["capo_rds.types.string.String"]
    """<p>A value that indicates the type of recommendation. This value determines how the description is rendered.</p>"""
    severity: NotRequired["capo_rds.types.string.String"]
    """<p>The severity level of the recommendation. The severity level can help you decide the urgency with which to address the recommendation.</p> <p>Valid values:</p> <ul> <li> <p> <code>high</code> </p> </li> <li> <p> <code>medium</code> </p> </li> <li> <p> <code>low</code> </p> </li> <li> <p> <code>informational</code> </p> </li> </ul>"""
    resource_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the RDS resource associated with the recommendation.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The current status of the recommendation.</p> <p>Valid values:</p> <ul> <li> <p> <code>active</code> - The recommendations which are ready for you to apply.</p> </li> <li> <p> <code>pending</code> - The applied or scheduled recommendations which are in progress.</p> </li> <li> <p> <code>resolved</code> - The recommendations which are completed.</p> </li> <li> <p> <code>dismissed</code> - The recommendations that you dismissed.</p> </li> </ul>"""
    created_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the recommendation was created. For example, <code>2023-09-28T01:13:53.931000+00:00</code>.</p>"""
    updated_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the recommendation was last updated.</p>"""
    detection: NotRequired["capo_rds.types.string.String"]
    """<p>A short description of the issue identified for this recommendation. The description might contain markdown.</p>"""
    recommendation: NotRequired["capo_rds.types.string.String"]
    """<p>A short description of the recommendation to resolve an issue. The description might contain markdown.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>A detailed description of the recommendation. The description might contain markdown.</p>"""
    reason: NotRequired["capo_rds.types.string.String"]
    """<p>The reason why this recommendation was created. The information might contain markdown.</p>"""
    recommended_actions: NotRequired[
        "capo_rds.types.recommended_action_list.RecommendedActionList"
    ]
    """<p>A list of recommended actions.</p>"""
    category: NotRequired["capo_rds.types.string.String"]
    """<p>The category of the recommendation.</p> <p>Valid values:</p> <ul> <li> <p> <code>performance efficiency</code> </p> </li> <li> <p> <code>security</code> </p> </li> <li> <p> <code>reliability</code> </p> </li> <li> <p> <code>cost optimization</code> </p> </li> <li> <p> <code>operational excellence</code> </p> </li> <li> <p> <code>sustainability</code> </p> </li> </ul>"""
    source: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services service that generated the recommendations.</p>"""
    type_detection: NotRequired["capo_rds.types.string.String"]
    """<p>A short description of the recommendation type. The description might contain markdown.</p>"""
    type_recommendation: NotRequired["capo_rds.types.string.String"]
    """<p>A short description that summarizes the recommendation to fix all the issues of the recommendation type. The description might contain markdown.</p>"""
    impact: NotRequired["capo_rds.types.string.String"]
    """<p>A short description that explains the possible impact of an issue.</p>"""
    additional_info: NotRequired["capo_rds.types.string.String"]
    """<p>Additional information about the recommendation. The information might contain markdown.</p>"""
    links: NotRequired["capo_rds.types.doc_link_list.DocLinkList"]
    """<p>A link to documentation that provides additional information about the recommendation.</p>"""
    issue_details: NotRequired["capo_rds.types.issue_details.IssueDetails"]
    """<p>Details of the issue that caused the recommendation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBRecommendation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "recommendation_id" in value:
        pairs.append((f"{prefix}.RecommendationId", str(value["recommendation_id"])))
    if "type_id" in value:
        pairs.append((f"{prefix}.TypeId", str(value["type_id"])))
    if "severity" in value:
        pairs.append((f"{prefix}.Severity", str(value["severity"])))
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "created_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["created_time"], pairs, f"{prefix}.CreatedTime"
        )
    if "updated_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["updated_time"], pairs, f"{prefix}.UpdatedTime"
        )
    if "detection" in value:
        pairs.append((f"{prefix}.Detection", str(value["detection"])))
    if "recommendation" in value:
        pairs.append((f"{prefix}.Recommendation", str(value["recommendation"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "reason" in value:
        pairs.append((f"{prefix}.Reason", str(value["reason"])))
    if "recommended_actions" in value:
        import capo_rds.types.recommended_action_list

        capo_rds.types.recommended_action_list.serialize_query(
            value["recommended_actions"], pairs, f"{prefix}.RecommendedActions"
        )
    if "category" in value:
        pairs.append((f"{prefix}.Category", str(value["category"])))
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "type_detection" in value:
        pairs.append((f"{prefix}.TypeDetection", str(value["type_detection"])))
    if "type_recommendation" in value:
        pairs.append(
            (f"{prefix}.TypeRecommendation", str(value["type_recommendation"]))
        )
    if "impact" in value:
        pairs.append((f"{prefix}.Impact", str(value["impact"])))
    if "additional_info" in value:
        pairs.append((f"{prefix}.AdditionalInfo", str(value["additional_info"])))
    if "links" in value:
        import capo_rds.types.doc_link_list

        capo_rds.types.doc_link_list.serialize_query(
            value["links"], pairs, f"{prefix}.Links"
        )
    if "issue_details" in value:
        import capo_rds.types.issue_details

        capo_rds.types.issue_details.serialize_query(
            value["issue_details"], pairs, f"{prefix}.IssueDetails"
        )


def deserialize_query(el: Element) -> DBRecommendation:
    out: DBRecommendation = {}  # type: ignore[typeddict-item]
    child_recommendation_id = el.find("RecommendationId")
    if child_recommendation_id is not None:
        out["recommendation_id"] = str(child_recommendation_id.text or "")
    child_type_id = el.find("TypeId")
    if child_type_id is not None:
        out["type_id"] = str(child_type_id.text or "")
    child_severity = el.find("Severity")
    if child_severity is not None:
        out["severity"] = str(child_severity.text or "")
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_rds.types.t_stamp

        out["created_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_created_time
        )
    child_updated_time = el.find("UpdatedTime")
    if child_updated_time is not None:
        import capo_rds.types.t_stamp

        out["updated_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_updated_time
        )
    child_detection = el.find("Detection")
    if child_detection is not None:
        out["detection"] = str(child_detection.text or "")
    child_recommendation = el.find("Recommendation")
    if child_recommendation is not None:
        out["recommendation"] = str(child_recommendation.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    child_recommended_actions = el.find("RecommendedActions")
    if child_recommended_actions is not None:
        import capo_rds.types.recommended_action_list

        out["recommended_actions"] = (
            capo_rds.types.recommended_action_list.deserialize_query(
                child_recommended_actions
            )
        )
    child_category = el.find("Category")
    if child_category is not None:
        out["category"] = str(child_category.text or "")
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_type_detection = el.find("TypeDetection")
    if child_type_detection is not None:
        out["type_detection"] = str(child_type_detection.text or "")
    child_type_recommendation = el.find("TypeRecommendation")
    if child_type_recommendation is not None:
        out["type_recommendation"] = str(child_type_recommendation.text or "")
    child_impact = el.find("Impact")
    if child_impact is not None:
        out["impact"] = str(child_impact.text or "")
    child_additional_info = el.find("AdditionalInfo")
    if child_additional_info is not None:
        out["additional_info"] = str(child_additional_info.text or "")
    child_links = el.find("Links")
    if child_links is not None:
        import capo_rds.types.doc_link_list

        out["links"] = capo_rds.types.doc_link_list.deserialize_query(child_links)
    child_issue_details = el.find("IssueDetails")
    if child_issue_details is not None:
        import capo_rds.types.issue_details

        out["issue_details"] = capo_rds.types.issue_details.deserialize_query(
            child_issue_details
        )
    return out
