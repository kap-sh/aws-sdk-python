"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppSessionMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.session_name
    import aws_sdk_qapps.types.session_sharing_configuration
    import aws_sdk_qapps.types.uuid


class UpdateQAppSessionMetadataOutput(TypedDict):
    session_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the updated Q App session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the updated Q App session.</p>"""
    session_name: NotRequired["aws_sdk_qapps.types.session_name.SessionName"]
    """<p>The new name of the updated Q App session.</p>"""
    sharing_configuration: (
        "aws_sdk_qapps.types.session_sharing_configuration.SessionSharingConfiguration"
    )
    """<p>The new sharing configuration of the updated Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppSessionMetadataOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    import aws_sdk_qapps.types.session_sharing_configuration

    out["sharingConfiguration"] = (
        aws_sdk_qapps.types.session_sharing_configuration.serialize_json(
            value["sharing_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQAppSessionMetadataOutput:
    out: UpdateQAppSessionMetadataOutput = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError(
            "UpdateQAppSessionMetadataOutput.session_id required"
        )
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError(
            "UpdateQAppSessionMetadataOutput.session_arn required"
        )
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
            "UpdateQAppSessionMetadataOutput.sharing_configuration required"
        )
    return out
