"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_version
    import aws_sdk_qapps.types.card_status_map
    import aws_sdk_qapps.types.execution_status
    import aws_sdk_qapps.types.session_name


class GetQAppSessionOutput(TypedDict):
    session_id: "str"
    """<p>The unique identifier of the Q App session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Q App session.</p>"""
    session_name: NotRequired["aws_sdk_qapps.types.session_name.SessionName"]
    """<p>The name of the Q App session.</p>"""
    app_version: NotRequired["aws_sdk_qapps.types.app_version.AppVersion"]
    """<p>The version of the Q App used for the session.</p>"""
    latest_published_app_version: NotRequired[
        "aws_sdk_qapps.types.app_version.AppVersion"
    ]
    """<p>The latest published version of the Q App used for the session.</p>"""
    status: "aws_sdk_qapps.types.execution_status.ExecutionStatus"
    """<p>The current status of the Q App session.</p>"""
    card_status: "aws_sdk_qapps.types.card_status_map.CardStatusMap"
    """<p>The current status for each card in the Q App session.</p>"""
    user_is_host: NotRequired["bool"]
    """<p>Indicates whether the current user is the owner of the Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppSessionOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    if "latest_published_app_version" in value:
        out["latestPublishedAppVersion"] = value["latest_published_app_version"]
    import aws_sdk_qapps.types.execution_status

    out["status"] = aws_sdk_qapps.types.execution_status.serialize_json(value["status"])
    import aws_sdk_qapps.types.card_status_map

    out["cardStatus"] = aws_sdk_qapps.types.card_status_map.serialize_json(
        value["card_status"]
    )
    if "user_is_host" in value:
        out["userIsHost"] = value["user_is_host"]
    return out


def deserialize_json(data: dict) -> GetQAppSessionOutput:
    out: GetQAppSessionOutput = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetQAppSessionOutput.session_id required")
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("GetQAppSessionOutput.session_arn required")
    if "sessionName" in data:
        out["session_name"] = data["sessionName"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    if "latestPublishedAppVersion" in data:
        out["latest_published_app_version"] = data["latestPublishedAppVersion"]
    if "status" in data:
        import aws_sdk_qapps.types.execution_status

        out["status"] = aws_sdk_qapps.types.execution_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetQAppSessionOutput.status required")
    if "cardStatus" in data:
        import aws_sdk_qapps.types.card_status_map

        out["card_status"] = aws_sdk_qapps.types.card_status_map.deserialize_json(
            data["cardStatus"]
        )
    else:
        raise DeserializationError("GetQAppSessionOutput.card_status required")
    if "userIsHost" in data:
        out["user_is_host"] = data["userIsHost"]
    return out
