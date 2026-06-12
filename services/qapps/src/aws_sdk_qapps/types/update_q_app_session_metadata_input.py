"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppSessionMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.session_name
    import aws_sdk_qapps.types.session_sharing_configuration
    import aws_sdk_qapps.types.uuid


class UpdateQAppSessionMetadataInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App session to update configuration for.</p>"""
    session_name: NotRequired["aws_sdk_qapps.types.session_name.SessionName"]
    """<p>The new name for the Q App session.</p>"""
    sharing_configuration: (
        "aws_sdk_qapps.types.session_sharing_configuration.SessionSharingConfiguration"
    )
    """<p>The new sharing configuration for the Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppSessionMetadataInput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    import aws_sdk_qapps.types.session_sharing_configuration

    out["sharingConfiguration"] = (
        aws_sdk_qapps.types.session_sharing_configuration.serialize_json(
            value["sharing_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQAppSessionMetadataInput:
    out: UpdateQAppSessionMetadataInput = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("UpdateQAppSessionMetadataInput.session_id required")
    if "sessionName" in data:
        out["session_name"] = data["sessionName"]
    if "sharingConfiguration" in data:
        import aws_sdk_qapps.types.session_sharing_configuration

        out["sharing_configuration"] = (
            aws_sdk_qapps.types.session_sharing_configuration.deserialize_json(
                data["sharingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQAppSessionMetadataInput.sharing_configuration required"
        )
    return out
