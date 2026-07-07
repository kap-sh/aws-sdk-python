"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantDetailsToAdd``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.display_name
    import aws_sdk_connect.types.participant_capabilities
    import aws_sdk_connect.types.participant_role


class ParticipantDetailsToAdd(TypedDict, closed=True):
    participant_role: NotRequired[
        "aws_sdk_connect.types.participant_role.ParticipantRole"
    ]
    """<p>The role of the participant being added.</p>"""
    display_name: NotRequired["aws_sdk_connect.types.display_name.DisplayName"]
    """<p>The display name of the participant.</p>"""
    participant_capabilities: NotRequired[
        "aws_sdk_connect.types.participant_capabilities.ParticipantCapabilities"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantDetailsToAdd) -> dict:
    out: dict = {}
    if "participant_role" in value:
        import aws_sdk_connect.types.participant_role

        out["ParticipantRole"] = aws_sdk_connect.types.participant_role.serialize_json(
            value["participant_role"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "participant_capabilities" in value:
        import aws_sdk_connect.types.participant_capabilities

        out["ParticipantCapabilities"] = (
            aws_sdk_connect.types.participant_capabilities.serialize_json(
                value["participant_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipantDetailsToAdd:
    out: ParticipantDetailsToAdd = {}  # type: ignore[typeddict-item]
    if "ParticipantRole" in data:
        import aws_sdk_connect.types.participant_role

        out["participant_role"] = (
            aws_sdk_connect.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ParticipantCapabilities" in data:
        import aws_sdk_connect.types.participant_capabilities

        out["participant_capabilities"] = (
            aws_sdk_connect.types.participant_capabilities.deserialize_json(
                data["ParticipantCapabilities"]
            )
        )
    return out
