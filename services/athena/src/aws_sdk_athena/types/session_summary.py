"""Generated from Smithy shape ``com.amazonaws.athena#SessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.engine_version
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.session_id
    import aws_sdk_athena.types.session_status


class SessionSummary(TypedDict):
    session_id: NotRequired["aws_sdk_athena.types.session_id.SessionId"]
    """<p>The session ID.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>The session description.</p>"""
    engine_version: NotRequired["aws_sdk_athena.types.engine_version.EngineVersion"]
    """<p>The engine version used by the session (for example, <code>PySpark engine version 3</code>).</p>"""
    notebook_version: NotRequired["aws_sdk_athena.types.name_string.NameString"]
    """<p>The notebook version.</p>"""
    status: NotRequired["aws_sdk_athena.types.session_status.SessionStatus"]
    """<p>Contains information about the session status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionSummary) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "engine_version" in value:
        import aws_sdk_athena.types.engine_version

        out["EngineVersion"] = (
            aws_sdk_athena.types.engine_version.serialize_aws_json_1_1(
                value["engine_version"]
            )
        )
    if "notebook_version" in value:
        out["NotebookVersion"] = value["notebook_version"]
    if "status" in value:
        import aws_sdk_athena.types.session_status

        out["Status"] = aws_sdk_athena.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EngineVersion" in data:
        import aws_sdk_athena.types.engine_version

        out["engine_version"] = (
            aws_sdk_athena.types.engine_version.deserialize_aws_json_1_1(
                data["EngineVersion"]
            )
        )
    if "NotebookVersion" in data:
        out["notebook_version"] = data["NotebookVersion"]
    if "Status" in data:
        import aws_sdk_athena.types.session_status

        out["status"] = aws_sdk_athena.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
