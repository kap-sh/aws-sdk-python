"""Generated from Smithy shape ``com.amazonaws.ssm#Session``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.access_type
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.max_session_duration
    import aws_sdk_ssm.types.session_details
    import aws_sdk_ssm.types.session_id
    import aws_sdk_ssm.types.session_manager_output_url
    import aws_sdk_ssm.types.session_owner
    import aws_sdk_ssm.types.session_reason
    import aws_sdk_ssm.types.session_status
    import aws_sdk_ssm.types.session_target


class Session(TypedDict):
    session_id: NotRequired["aws_sdk_ssm.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""
    target: NotRequired["aws_sdk_ssm.types.session_target.SessionTarget"]
    """<p>The managed node that the Session Manager session connected to.</p>"""
    status: NotRequired["aws_sdk_ssm.types.session_status.SessionStatus"]
    r"""<p>The status of the session. For example, \"Connected\" or \"Terminated\".</p>"""
    start_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time, in ISO-8601 Extended format, when the session began.</p>"""
    end_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time, in ISO-8601 Extended format, when the session was terminated.</p>"""
    document_name: NotRequired["aws_sdk_ssm.types.document_name.DocumentName"]
    """<p>The name of the Session Manager SSM document used to define the parameters and plugin settings for the session. For example, <code>SSM-SessionManagerRunShell</code>.</p>"""
    owner: NotRequired["aws_sdk_ssm.types.session_owner.SessionOwner"]
    """<p>The ID of the Amazon Web Services user that started the session.</p>"""
    reason: NotRequired["aws_sdk_ssm.types.session_reason.SessionReason"]
    """<p>The reason for connecting to the instance.</p>"""
    details: NotRequired["aws_sdk_ssm.types.session_details.SessionDetails"]
    """<p>Reserved for future use.</p>"""
    output_url: NotRequired[
        "aws_sdk_ssm.types.session_manager_output_url.SessionManagerOutputUrl"
    ]
    """<p>Reserved for future use.</p>"""
    max_session_duration: NotRequired[
        "aws_sdk_ssm.types.max_session_duration.MaxSessionDuration"
    ]
    """<p>The maximum duration of a session before it terminates.</p>"""
    access_type: NotRequired["aws_sdk_ssm.types.access_type.AccessType"]
    r"""<p> <code>Standard</code> access type is the default for Session Manager sessions. <code>JustInTime</code> is the access type for <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html\">Just-in-time node access</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "target" in value:
        out["Target"] = value["target"]
    if "status" in value:
        import aws_sdk_ssm.types.session_status

        out["Status"] = aws_sdk_ssm.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "start_date" in value:
        import aws_sdk_ssm.types.date_time

        out["StartDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_date"]
        )
    if "end_date" in value:
        import aws_sdk_ssm.types.date_time

        out["EndDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_date"]
        )
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "details" in value:
        out["Details"] = value["details"]
    if "output_url" in value:
        import aws_sdk_ssm.types.session_manager_output_url

        out["OutputUrl"] = (
            aws_sdk_ssm.types.session_manager_output_url.serialize_aws_json_1_1(
                value["output_url"]
            )
        )
    if "max_session_duration" in value:
        out["MaxSessionDuration"] = value["max_session_duration"]
    if "access_type" in value:
        import aws_sdk_ssm.types.access_type

        out["AccessType"] = aws_sdk_ssm.types.access_type.serialize_aws_json_1_1(
            value["access_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "Status" in data:
        import aws_sdk_ssm.types.session_status

        out["status"] = aws_sdk_ssm.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StartDate" in data:
        import aws_sdk_ssm.types.date_time

        out["start_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartDate"]
        )
    if "EndDate" in data:
        import aws_sdk_ssm.types.date_time

        out["end_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndDate"]
        )
    if "DocumentName" in data:
        out["document_name"] = data["DocumentName"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "Details" in data:
        out["details"] = data["Details"]
    if "OutputUrl" in data:
        import aws_sdk_ssm.types.session_manager_output_url

        out["output_url"] = (
            aws_sdk_ssm.types.session_manager_output_url.deserialize_aws_json_1_1(
                data["OutputUrl"]
            )
        )
    if "MaxSessionDuration" in data:
        out["max_session_duration"] = data["MaxSessionDuration"]
    if "AccessType" in data:
        import aws_sdk_ssm.types.access_type

        out["access_type"] = aws_sdk_ssm.types.access_type.deserialize_aws_json_1_1(
            data["AccessType"]
        )
    return out
