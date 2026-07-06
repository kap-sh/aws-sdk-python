"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.evaluation_form_version_is_locked
    import aws_sdk_connect.types.evaluation_form_version_status
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.version_number


class EvaluationFormVersionSummary(TypedDict, closed=True):
    evaluation_form_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "aws_sdk_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    locked: "aws_sdk_connect.types.evaluation_form_version_is_locked.EvaluationFormVersionIsLocked"
    """<p>The flag indicating whether the evaluation form is locked for changes.</p>"""
    status: "aws_sdk_connect.types.evaluation_form_version_status.EvaluationFormVersionStatus"
    """<p>The status of the evaluation form.</p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was created.</p>"""
    created_by: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who created the evaluation form.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was last updated.</p>"""
    last_modified_by: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormVersionSummary) -> dict:
    out: dict = {}
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    out["Locked"] = value.get("locked", False)
    import aws_sdk_connect.types.evaluation_form_version_status

    out["Status"] = aws_sdk_connect.types.evaluation_form_version_status.serialize_json(
        value["status"]
    )
    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    out["CreatedBy"] = value["created_by"]
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["LastModifiedBy"] = value["last_modified_by"]
    return out


def deserialize_json(data: dict) -> EvaluationFormVersionSummary:
    out: EvaluationFormVersionSummary = {}  # type: ignore[typeddict-item]
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError(
            "EvaluationFormVersionSummary.evaluation_form_arn required"
        )
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError(
            "EvaluationFormVersionSummary.evaluation_form_id required"
        )
    if "EvaluationFormVersion" in data:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if "Locked" in data:
        out["locked"] = data["Locked"]
    else:
        out["locked"] = False
    if "Status" in data:
        import aws_sdk_connect.types.evaluation_form_version_status

        out["status"] = (
            aws_sdk_connect.types.evaluation_form_version_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationFormVersionSummary.status required")
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationFormVersionSummary.created_time required")
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    else:
        raise DeserializationError("EvaluationFormVersionSummary.created_by required")
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError(
            "EvaluationFormVersionSummary.last_modified_time required"
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    else:
        raise DeserializationError(
            "EvaluationFormVersionSummary.last_modified_by required"
        )
    return out
