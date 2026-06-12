"""Generated from Smithy shape ``com.amazonaws.qapps#StartQAppSessionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_version
    import aws_sdk_qapps.types.card_value_list
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.tag_map
    import aws_sdk_qapps.types.uuid


class StartQAppSessionInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to start a session for.</p>"""
    app_version: "aws_sdk_qapps.types.app_version.AppVersion"
    """<p>The version of the Q App to use for the session.</p>"""
    initial_values: NotRequired["aws_sdk_qapps.types.card_value_list.CardValueList"]
    """<p>Optional initial input values to provide for the Q App session.</p>"""
    session_id: NotRequired["str"]
    """<p>The unique identifier of the a Q App session.</p>"""
    tags: NotRequired["aws_sdk_qapps.types.tag_map.TagMap"]
    """<p>Optional tags to associate with the new Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQAppSessionInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appVersion"] = value["app_version"]
    if "initial_values" in value:
        import aws_sdk_qapps.types.card_value_list

        out["initialValues"] = aws_sdk_qapps.types.card_value_list.serialize_json(
            value["initial_values"]
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "tags" in value:
        import aws_sdk_qapps.types.tag_map

        out["tags"] = aws_sdk_qapps.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartQAppSessionInput:
    out: StartQAppSessionInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("StartQAppSessionInput.app_id required")
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("StartQAppSessionInput.app_version required")
    if "initialValues" in data:
        import aws_sdk_qapps.types.card_value_list

        out["initial_values"] = aws_sdk_qapps.types.card_value_list.deserialize_json(
            data["initialValues"]
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "tags" in data:
        import aws_sdk_qapps.types.tag_map

        out["tags"] = aws_sdk_qapps.types.tag_map.deserialize_json(data["tags"])
    return out
