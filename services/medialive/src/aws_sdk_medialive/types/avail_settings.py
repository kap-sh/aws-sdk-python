"""Generated from Smithy shape ``com.amazonaws.medialive#AvailSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.esam
    import aws_sdk_medialive.types.scte35_splice_insert
    import aws_sdk_medialive.types.scte35_time_signal_apos


class AvailSettings(TypedDict):
    esam: NotRequired["aws_sdk_medialive.types.esam.Esam"]
    scte35_splice_insert: NotRequired[
        "aws_sdk_medialive.types.scte35_splice_insert.Scte35SpliceInsert"
    ]
    scte35_time_signal_apos: NotRequired[
        "aws_sdk_medialive.types.scte35_time_signal_apos.Scte35TimeSignalApos"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AvailSettings) -> dict:
    out: dict = {}
    if "esam" in value:
        import aws_sdk_medialive.types.esam

        out["esam"] = aws_sdk_medialive.types.esam.serialize_json(value["esam"])
    if "scte35_splice_insert" in value:
        import aws_sdk_medialive.types.scte35_splice_insert

        out["scte35SpliceInsert"] = (
            aws_sdk_medialive.types.scte35_splice_insert.serialize_json(
                value["scte35_splice_insert"]
            )
        )
    if "scte35_time_signal_apos" in value:
        import aws_sdk_medialive.types.scte35_time_signal_apos

        out["scte35TimeSignalApos"] = (
            aws_sdk_medialive.types.scte35_time_signal_apos.serialize_json(
                value["scte35_time_signal_apos"]
            )
        )
    return out


def deserialize_json(data: dict) -> AvailSettings:
    out: AvailSettings = {}  # type: ignore[typeddict-item]
    if "esam" in data:
        import aws_sdk_medialive.types.esam

        out["esam"] = aws_sdk_medialive.types.esam.deserialize_json(data["esam"])
    if "scte35SpliceInsert" in data:
        import aws_sdk_medialive.types.scte35_splice_insert

        out["scte35_splice_insert"] = (
            aws_sdk_medialive.types.scte35_splice_insert.deserialize_json(
                data["scte35SpliceInsert"]
            )
        )
    if "scte35TimeSignalApos" in data:
        import aws_sdk_medialive.types.scte35_time_signal_apos

        out["scte35_time_signal_apos"] = (
            aws_sdk_medialive.types.scte35_time_signal_apos.deserialize_json(
                data["scte35TimeSignalApos"]
            )
        )
    return out
