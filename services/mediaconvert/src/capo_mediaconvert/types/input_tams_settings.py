"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputTamsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_pattern019090190908019090190908
    import capo_mediaconvert.types.__string_pattern_arn_aws_az09_events_az090912_connection_azaz09_af0936
    import capo_mediaconvert.types.tams_gap_handling


class InputTamsSettings(TypedDict, closed=True):
    auth_connection_arn: NotRequired[
        "capo_mediaconvert.types.__string_pattern_arn_aws_az09_events_az090912_connection_azaz09_af0936.__stringPatternArnAwsAZ09EventsAZ090912ConnectionAZAZ09AF0936"
    ]
    """Specify the ARN (Amazon Resource Name) of an EventBridge Connection to authenticate with your TAMS server. The EventBridge Connection stores your authentication credentials securely. MediaConvert assumes your job's IAM role to access this connection, so ensure the role has the events:RetrieveConnectionCredentials, secretsmanager:DescribeSecret, and secretsmanager:GetSecretValue permissions. Format: arn:aws:events:region:account-id:connection/connection-name/unique-id This setting is required when you include TAMS settings in your job."""
    gap_handling: NotRequired[
        "capo_mediaconvert.types.tams_gap_handling.TamsGapHandling"
    ]
    """Specify how MediaConvert handles gaps between media segments in your TAMS source. Gaps can occur in live streams due to network issues or other interruptions. Choose from the following options: * Skip gaps - Default. Skip over gaps and join segments together. This creates a continuous output with no blank frames, but may cause timeline discontinuities. * Fill with black - Insert black frames to fill gaps between segments. This maintains timeline continuity but adds black frames where content is missing. * Hold last frame - Repeat the last frame before a gap until the next segment begins. This maintains visual continuity during gaps."""
    source_id: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Specify the unique identifier for the media source in your TAMS server. MediaConvert uses this source ID to locate the appropriate flows containing the media segments you want to process. The source ID corresponds to a specific media source registered in your TAMS server. This source must be of type urn:x-nmos:format:multi, and can can reference multiple flows for audio, video, or combined audio/video content. MediaConvert automatically selects the highest quality flows available for your job. This setting is required when you include TAMS settings in your job."""
    timerange: NotRequired[
        "capo_mediaconvert.types.__string_pattern019090190908019090190908.__stringPattern019090190908019090190908"
    ]
    """Specify the time range of media segments to retrieve from your TAMS server. MediaConvert fetches only the segments that fall within this range. Use the format specified by your TAMS server implementation. This must be two timestamp values with the format {sign?}{seconds}:{nanoseconds}, separated by an underscore, surrounded by either parentheses or square brackets. Example: [15:0_35:0) This setting is required when you include TAMS settings in your job."""


# --- restJson1 ser/de ---
def serialize_json(value: InputTamsSettings) -> dict:
    out: dict = {}
    if "auth_connection_arn" in value:
        out["authConnectionArn"] = value["auth_connection_arn"]
    if "gap_handling" in value:
        import capo_mediaconvert.types.tams_gap_handling

        out["gapHandling"] = capo_mediaconvert.types.tams_gap_handling.serialize_json(
            value["gap_handling"]
        )
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "timerange" in value:
        out["timerange"] = value["timerange"]
    return out


def deserialize_json(data: dict) -> InputTamsSettings:
    out: InputTamsSettings = {}  # type: ignore[typeddict-item]
    if "authConnectionArn" in data:
        out["auth_connection_arn"] = data["authConnectionArn"]
    if "gapHandling" in data:
        import capo_mediaconvert.types.tams_gap_handling

        out["gap_handling"] = (
            capo_mediaconvert.types.tams_gap_handling.deserialize_json(
                data["gapHandling"]
            )
        )
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "timerange" in data:
        out["timerange"] = data["timerange"]
    return out
