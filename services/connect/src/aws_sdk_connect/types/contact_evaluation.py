"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_arn
    import aws_sdk_connect.types.export_location
    import aws_sdk_connect.types.form_id
    import aws_sdk_connect.types.status
    import aws_sdk_connect.types.timestamp


class ContactEvaluation(TypedDict, closed=True):
    form_id: NotRequired["aws_sdk_connect.types.form_id.FormId"]
    """<p>The <code>FormId</code> of the contact evaluation.</p>"""
    evaluation_arn: NotRequired["aws_sdk_connect.types.evaluation_arn.EvaluationArn"]
    """<p>The Amazon Resource Name for the evaluation form. It is always present.</p>"""
    status: NotRequired["aws_sdk_connect.types.status.Status"]
    """<p>The status of the evaluation.</p>"""
    start_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the evaluation was started, in UTC time.</p>"""
    end_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the evaluation was submitted, in UTC time.</p>"""
    delete_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the evaluation was deleted, in UTC time.</p>"""
    export_location: NotRequired["aws_sdk_connect.types.export_location.ExportLocation"]
    """<p>The path where evaluation was exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluation) -> dict:
    out: dict = {}
    if "form_id" in value:
        out["FormId"] = value["form_id"]
    if "evaluation_arn" in value:
        out["EvaluationArn"] = value["evaluation_arn"]
    if "status" in value:
        import aws_sdk_connect.types.status

        out["Status"] = aws_sdk_connect.types.status.serialize_json(value["status"])
    if "start_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["StartTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["start_timestamp"]
        )
    if "end_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["EndTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["end_timestamp"]
        )
    if "delete_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["DeleteTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["delete_timestamp"]
        )
    if "export_location" in value:
        out["ExportLocation"] = value["export_location"]
    return out


def deserialize_json(data: dict) -> ContactEvaluation:
    out: ContactEvaluation = {}  # type: ignore[typeddict-item]
    if "FormId" in data:
        out["form_id"] = data["FormId"]
    if "EvaluationArn" in data:
        out["evaluation_arn"] = data["EvaluationArn"]
    if "Status" in data:
        import aws_sdk_connect.types.status

        out["status"] = aws_sdk_connect.types.status.deserialize_json(data["Status"])
    if "StartTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["start_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["StartTimestamp"]
        )
    if "EndTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["end_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["EndTimestamp"]
        )
    if "DeleteTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["delete_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["DeleteTimestamp"]
        )
    if "ExportLocation" in data:
        out["export_location"] = data["ExportLocation"]
    return out
