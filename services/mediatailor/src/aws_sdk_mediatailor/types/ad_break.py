"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdBreak``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__long
    import aws_sdk_mediatailor.types.ad_break_metadata_list
    import aws_sdk_mediatailor.types.message_type
    import aws_sdk_mediatailor.types.slate_source
    import aws_sdk_mediatailor.types.splice_insert_message
    import aws_sdk_mediatailor.types.time_signal_message


class AdBreak(TypedDict, closed=True):
    message_type: NotRequired["aws_sdk_mediatailor.types.message_type.MessageType"]
    """<p>The SCTE-35 ad insertion type. Accepted value: <code>SPLICE_INSERT</code>, <code>TIME_SIGNAL</code>.</p>"""
    offset_millis: "aws_sdk_mediatailor.types.__long.__long"
    """<p>How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.</p>"""
    slate: NotRequired["aws_sdk_mediatailor.types.slate_source.SlateSource"]
    """<p>Ad break slate configuration.</p>"""
    splice_insert_message: NotRequired[
        "aws_sdk_mediatailor.types.splice_insert_message.SpliceInsertMessage"
    ]
    """<p>This defines the SCTE-35 <code>splice_insert()</code> message inserted around the ad. For information about using <code>splice_insert()</code>, see the SCTE-35 specficiaiton, section 9.7.3.1.</p>"""
    time_signal_message: NotRequired[
        "aws_sdk_mediatailor.types.time_signal_message.TimeSignalMessage"
    ]
    """<p>Defines the SCTE-35 <code>time_signal</code> message inserted around the ad.</p> <p>Programs on a channel's schedule can be configured with one or more ad breaks. You can attach a <code>splice_insert</code> SCTE-35 message to the ad break. This message provides basic metadata about the ad break.</p> <p>See section 9.7.4 of the 2022 SCTE-35 specification for more information.</p>"""
    ad_break_metadata: NotRequired[
        "aws_sdk_mediatailor.types.ad_break_metadata_list.AdBreakMetadataList"
    ]
    """<p>Defines a list of key/value pairs that MediaTailor generates within the <code>EXT-X-ASSET</code>tag for <code>SCTE35_ENHANCED</code> output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdBreak) -> dict:
    out: dict = {}
    if "message_type" in value:
        import aws_sdk_mediatailor.types.message_type

        out["MessageType"] = aws_sdk_mediatailor.types.message_type.serialize_json(
            value["message_type"]
        )
    out["OffsetMillis"] = value.get("offset_millis", 0)
    if "slate" in value:
        import aws_sdk_mediatailor.types.slate_source

        out["Slate"] = aws_sdk_mediatailor.types.slate_source.serialize_json(
            value["slate"]
        )
    if "splice_insert_message" in value:
        import aws_sdk_mediatailor.types.splice_insert_message

        out["SpliceInsertMessage"] = (
            aws_sdk_mediatailor.types.splice_insert_message.serialize_json(
                value["splice_insert_message"]
            )
        )
    if "time_signal_message" in value:
        import aws_sdk_mediatailor.types.time_signal_message

        out["TimeSignalMessage"] = (
            aws_sdk_mediatailor.types.time_signal_message.serialize_json(
                value["time_signal_message"]
            )
        )
    if "ad_break_metadata" in value:
        import aws_sdk_mediatailor.types.ad_break_metadata_list

        out["AdBreakMetadata"] = (
            aws_sdk_mediatailor.types.ad_break_metadata_list.serialize_json(
                value["ad_break_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdBreak:
    out: AdBreak = {}  # type: ignore[typeddict-item]
    if "MessageType" in data:
        import aws_sdk_mediatailor.types.message_type

        out["message_type"] = aws_sdk_mediatailor.types.message_type.deserialize_json(
            data["MessageType"]
        )
    if "OffsetMillis" in data:
        out["offset_millis"] = data["OffsetMillis"]
    else:
        out["offset_millis"] = 0
    if "Slate" in data:
        import aws_sdk_mediatailor.types.slate_source

        out["slate"] = aws_sdk_mediatailor.types.slate_source.deserialize_json(
            data["Slate"]
        )
    if "SpliceInsertMessage" in data:
        import aws_sdk_mediatailor.types.splice_insert_message

        out["splice_insert_message"] = (
            aws_sdk_mediatailor.types.splice_insert_message.deserialize_json(
                data["SpliceInsertMessage"]
            )
        )
    if "TimeSignalMessage" in data:
        import aws_sdk_mediatailor.types.time_signal_message

        out["time_signal_message"] = (
            aws_sdk_mediatailor.types.time_signal_message.deserialize_json(
                data["TimeSignalMessage"]
            )
        )
    if "AdBreakMetadata" in data:
        import aws_sdk_mediatailor.types.ad_break_metadata_list

        out["ad_break_metadata"] = (
            aws_sdk_mediatailor.types.ad_break_metadata_list.deserialize_json(
                data["AdBreakMetadata"]
            )
        )
    return out
