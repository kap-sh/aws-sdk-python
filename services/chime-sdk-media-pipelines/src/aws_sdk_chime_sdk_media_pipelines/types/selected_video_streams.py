"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SelectedVideoStreams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.attendee_id_list
    import aws_sdk_chime_sdk_media_pipelines.types.external_user_id_list


class SelectedVideoStreams(TypedDict, closed=True):
    attendee_ids: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.attendee_id_list.AttendeeIdList"
    ]
    """<p>The attendee IDs of the streams selected for a media pipeline. </p>"""
    external_user_ids: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.external_user_id_list.ExternalUserIdList"
    ]
    """<p>The external user IDs of the streams selected for a media pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectedVideoStreams) -> dict:
    out: dict = {}
    if "attendee_ids" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.attendee_id_list

        out["AttendeeIds"] = (
            aws_sdk_chime_sdk_media_pipelines.types.attendee_id_list.serialize_json(
                value["attendee_ids"]
            )
        )
    if "external_user_ids" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.external_user_id_list

        out["ExternalUserIds"] = (
            aws_sdk_chime_sdk_media_pipelines.types.external_user_id_list.serialize_json(
                value["external_user_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectedVideoStreams:
    out: SelectedVideoStreams = {}  # type: ignore[typeddict-item]
    if "AttendeeIds" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.attendee_id_list

        out["attendee_ids"] = (
            aws_sdk_chime_sdk_media_pipelines.types.attendee_id_list.deserialize_json(
                data["AttendeeIds"]
            )
        )
    if "ExternalUserIds" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.external_user_id_list

        out["external_user_ids"] = (
            aws_sdk_chime_sdk_media_pipelines.types.external_user_id_list.deserialize_json(
                data["ExternalUserIds"]
            )
        )
    return out
