"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.boolean
    import capo_connect.types.contact_interaction_type
    import capo_connect.types.evaluation_form_description
    import capo_connect.types.evaluation_form_language_code
    import capo_connect.types.evaluation_form_title
    import capo_connect.types.evaluation_form_version_status
    import capo_connect.types.resource_id
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class EvaluationFormSearchSummary(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>The title of the evaluation form.</p>"""
    status: (
        "capo_connect.types.evaluation_form_version_status.EvaluationFormVersionStatus"
    )
    """<p>The status of the evaluation form.</p>"""
    description: NotRequired[
        "capo_connect.types.evaluation_form_description.EvaluationFormDescription"
    ]
    """<p>The description of the evaluation form.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>When the evaluation form was created.</p>"""
    created_by: "capo_connect.types.arn.ARN"
    """<p>Who created the evaluation form.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>When the evaluation form was last changed.</p>"""
    last_modified_by: "capo_connect.types.arn.ARN"
    """<p>Who changed the evaluation form.</p>"""
    last_activated_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>When the evaluation format was last activated.</p>"""
    last_activated_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The ID of user who last activated evaluation form.</p>"""
    latest_version: "capo_connect.types.version_number.VersionNumber"
    """<p>Latest version of the evaluation form.</p>"""
    active_version: NotRequired["capo_connect.types.version_number.VersionNumber"]
    """<p>Active version of the evaluation form.</p>"""
    auto_evaluation_enabled: "capo_connect.types.boolean.Boolean"
    """<p>Whether automated evaluation is enabled.</p>"""
    evaluation_form_language: NotRequired[
        "capo_connect.types.evaluation_form_language_code.EvaluationFormLanguageCode"
    ]
    """<p>The language of the evaluation form.</p>"""
    contact_interaction_type: NotRequired[
        "capo_connect.types.contact_interaction_type.ContactInteractionType"
    ]
    """<p>The contact interaction type for this evaluation form.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSearchSummary) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
    import capo_connect.types.evaluation_form_version_status

    out["Status"] = capo_connect.types.evaluation_form_version_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    out["CreatedBy"] = value["created_by"]
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["LastModifiedBy"] = value["last_modified_by"]
    if "last_activated_time" in value:
        import capo_connect.types.timestamp

        out["LastActivatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_activated_time"]
        )
    if "last_activated_by" in value:
        out["LastActivatedBy"] = value["last_activated_by"]
    out["LatestVersion"] = value["latest_version"]
    if "active_version" in value:
        out["ActiveVersion"] = value["active_version"]
    out["AutoEvaluationEnabled"] = value.get("auto_evaluation_enabled", False)
    if "evaluation_form_language" in value:
        import capo_connect.types.evaluation_form_language_code

        out["EvaluationFormLanguage"] = (
            capo_connect.types.evaluation_form_language_code.serialize_json(
                value["evaluation_form_language"]
            )
        )
    if "contact_interaction_type" in value:
        import capo_connect.types.contact_interaction_type

        out["ContactInteractionType"] = (
            capo_connect.types.contact_interaction_type.serialize_json(
                value["contact_interaction_type"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EvaluationFormSearchSummary:
    out: EvaluationFormSearchSummary = {}  # type: ignore[typeddict-item]
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError(
            "EvaluationFormSearchSummary.evaluation_form_id required"
        )
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError(
            "EvaluationFormSearchSummary.evaluation_form_arn required"
        )
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationFormSearchSummary.title required")
    if "Status" in data:
        import capo_connect.types.evaluation_form_version_status

        out["status"] = (
            capo_connect.types.evaluation_form_version_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationFormSearchSummary.status required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationFormSearchSummary.created_time required")
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    else:
        raise DeserializationError("EvaluationFormSearchSummary.created_by required")
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError(
            "EvaluationFormSearchSummary.last_modified_time required"
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    else:
        raise DeserializationError(
            "EvaluationFormSearchSummary.last_modified_by required"
        )
    if "LastActivatedTime" in data:
        import capo_connect.types.timestamp

        out["last_activated_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastActivatedTime"]
        )
    if "LastActivatedBy" in data:
        out["last_activated_by"] = data["LastActivatedBy"]
    if "LatestVersion" in data:
        out["latest_version"] = data["LatestVersion"]
    else:
        raise DeserializationError(
            "EvaluationFormSearchSummary.latest_version required"
        )
    if "ActiveVersion" in data:
        out["active_version"] = data["ActiveVersion"]
    if "AutoEvaluationEnabled" in data:
        out["auto_evaluation_enabled"] = data["AutoEvaluationEnabled"]
    else:
        out["auto_evaluation_enabled"] = False
    if "EvaluationFormLanguage" in data:
        import capo_connect.types.evaluation_form_language_code

        out["evaluation_form_language"] = (
            capo_connect.types.evaluation_form_language_code.deserialize_json(
                data["EvaluationFormLanguage"]
            )
        )
    if "ContactInteractionType" in data:
        import capo_connect.types.contact_interaction_type

        out["contact_interaction_type"] = (
            capo_connect.types.contact_interaction_type.deserialize_json(
                data["ContactInteractionType"]
            )
        )
    if "Tags" in data:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
