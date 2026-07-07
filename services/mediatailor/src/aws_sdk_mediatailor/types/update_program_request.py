"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_ad_break
    import aws_sdk_mediatailor.types.__list_of_audience_media
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.update_program_schedule_configuration


class UpdateProgramRequest(TypedDict, closed=True):
    ad_breaks: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
    ]
    """<p>The ad break configuration settings.</p>"""
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel for this Program.</p>"""
    program_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the Program.</p>"""
    schedule_configuration: "aws_sdk_mediatailor.types.update_program_schedule_configuration.UpdateProgramScheduleConfiguration"
    """<p>The schedule configuration settings.</p>"""
    audience_media: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
    ]
    """<p>The list of AudienceMedia defined in program.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProgramRequest) -> dict:
    out: dict = {}
    if "ad_breaks" in value:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["AdBreaks"] = aws_sdk_mediatailor.types.__list_of_ad_break.serialize_json(
            value["ad_breaks"]
        )
    import aws_sdk_mediatailor.types.update_program_schedule_configuration

    out["ScheduleConfiguration"] = (
        aws_sdk_mediatailor.types.update_program_schedule_configuration.serialize_json(
            value["schedule_configuration"]
        )
    )
    if "audience_media" in value:
        import aws_sdk_mediatailor.types.__list_of_audience_media

        out["AudienceMedia"] = (
            aws_sdk_mediatailor.types.__list_of_audience_media.serialize_json(
                value["audience_media"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateProgramRequest:
    out: UpdateProgramRequest = {}  # type: ignore[typeddict-item]
    if "AdBreaks" in data:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["ad_breaks"] = (
            aws_sdk_mediatailor.types.__list_of_ad_break.deserialize_json(
                data["AdBreaks"]
            )
        )
    if "ScheduleConfiguration" in data:
        import aws_sdk_mediatailor.types.update_program_schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_mediatailor.types.update_program_schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProgramRequest.schedule_configuration required"
        )
    if "AudienceMedia" in data:
        import aws_sdk_mediatailor.types.__list_of_audience_media

        out["audience_media"] = (
            aws_sdk_mediatailor.types.__list_of_audience_media.deserialize_json(
                data["AudienceMedia"]
            )
        )
    return out
