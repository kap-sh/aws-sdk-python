"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.audiences
    import aws_sdk_mediatailor.types.request_outputs
    import aws_sdk_mediatailor.types.slate_source
    import aws_sdk_mediatailor.types.time_shift_configuration


class UpdateChannelRequest(TypedDict):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""
    filler_slate: NotRequired["aws_sdk_mediatailor.types.slate_source.SlateSource"]
    """<p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>"""
    outputs: "aws_sdk_mediatailor.types.request_outputs.RequestOutputs"
    """<p>The channel's output properties.</p>"""
    time_shift_configuration: NotRequired[
        "aws_sdk_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
    ]
    """<p> The time-shifted viewing configuration you want to associate to the channel. </p>"""
    audiences: NotRequired["aws_sdk_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "filler_slate" in value:
        import aws_sdk_mediatailor.types.slate_source

        out["FillerSlate"] = aws_sdk_mediatailor.types.slate_source.serialize_json(
            value["filler_slate"]
        )
    import aws_sdk_mediatailor.types.request_outputs

    out["Outputs"] = aws_sdk_mediatailor.types.request_outputs.serialize_json(
        value["outputs"]
    )
    if "time_shift_configuration" in value:
        import aws_sdk_mediatailor.types.time_shift_configuration

        out["TimeShiftConfiguration"] = (
            aws_sdk_mediatailor.types.time_shift_configuration.serialize_json(
                value["time_shift_configuration"]
            )
        )
    if "audiences" in value:
        import aws_sdk_mediatailor.types.audiences

        out["Audiences"] = aws_sdk_mediatailor.types.audiences.serialize_json(
            value["audiences"]
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "FillerSlate" in data:
        import aws_sdk_mediatailor.types.slate_source

        out["filler_slate"] = aws_sdk_mediatailor.types.slate_source.deserialize_json(
            data["FillerSlate"]
        )
    if "Outputs" in data:
        import aws_sdk_mediatailor.types.request_outputs

        out["outputs"] = aws_sdk_mediatailor.types.request_outputs.deserialize_json(
            data["Outputs"]
        )
    else:
        raise DeserializationError("UpdateChannelRequest.outputs required")
    if "TimeShiftConfiguration" in data:
        import aws_sdk_mediatailor.types.time_shift_configuration

        out["time_shift_configuration"] = (
            aws_sdk_mediatailor.types.time_shift_configuration.deserialize_json(
                data["TimeShiftConfiguration"]
            )
        )
    if "Audiences" in data:
        import aws_sdk_mediatailor.types.audiences

        out["audiences"] = aws_sdk_mediatailor.types.audiences.deserialize_json(
            data["Audiences"]
        )
    return out
