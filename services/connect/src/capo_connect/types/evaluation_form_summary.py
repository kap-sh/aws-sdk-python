"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_form_title
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class EvaluationFormSummary(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>A title of the evaluation form.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was created.</p>"""
    created_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who created the evaluation form.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was last updated.</p>"""
    last_modified_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation form.</p>"""
    last_activated_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp for when the evaluation form was last activated.</p>"""
    last_activated_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p> The Amazon Resource Name (ARN) of the user who last activated the evaluation form.</p>"""
    latest_version: "capo_connect.types.version_number.VersionNumber"
    """<p>The version number of the latest evaluation form version.</p>"""
    active_version: NotRequired["capo_connect.types.version_number.VersionNumber"]
    """<p>The version of the active evaluation form version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSummary) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
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
    out["LatestVersion"] = value.get("latest_version", 0)
    if "active_version" in value:
        out["ActiveVersion"] = value["active_version"]
    return out


def deserialize_json(data: dict) -> EvaluationFormSummary:
    out: EvaluationFormSummary = {}  # type: ignore[typeddict-item]
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError("EvaluationFormSummary.evaluation_form_id required")
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError("EvaluationFormSummary.evaluation_form_arn required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationFormSummary.title required")
    if "CreatedTime" in data:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationFormSummary.created_time required")
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    else:
        raise DeserializationError("EvaluationFormSummary.created_by required")
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("EvaluationFormSummary.last_modified_time required")
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    else:
        raise DeserializationError("EvaluationFormSummary.last_modified_by required")
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
        out["latest_version"] = 0
    if "ActiveVersion" in data:
        out["active_version"] = data["ActiveVersion"]
    return out
