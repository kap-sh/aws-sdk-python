"""Generated from Smithy shape ``com.amazonaws.medialive#AvailSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.esam
    import capo_medialive.types.scte35_splice_insert
    import capo_medialive.types.scte35_time_signal_apos


class AvailSettings(TypedDict, closed=True):
    esam: NotRequired["capo_medialive.types.esam.Esam"]
    scte35_splice_insert: NotRequired[
        "capo_medialive.types.scte35_splice_insert.Scte35SpliceInsert"
    ]
    scte35_time_signal_apos: NotRequired[
        "capo_medialive.types.scte35_time_signal_apos.Scte35TimeSignalApos"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AvailSettings) -> dict:
    out: dict = {}
    if "esam" in value:
        import capo_medialive.types.esam

        out["esam"] = capo_medialive.types.esam.serialize_json(value["esam"])
    if "scte35_splice_insert" in value:
        import capo_medialive.types.scte35_splice_insert

        out["scte35SpliceInsert"] = (
            capo_medialive.types.scte35_splice_insert.serialize_json(
                value["scte35_splice_insert"]
            )
        )
    if "scte35_time_signal_apos" in value:
        import capo_medialive.types.scte35_time_signal_apos

        out["scte35TimeSignalApos"] = (
            capo_medialive.types.scte35_time_signal_apos.serialize_json(
                value["scte35_time_signal_apos"]
            )
        )
    return out


def deserialize_json(data: dict) -> AvailSettings:
    out: AvailSettings = {}  # type: ignore[typeddict-item]
    if "esam" in data:
        import capo_medialive.types.esam

        out["esam"] = capo_medialive.types.esam.deserialize_json(data["esam"])
    if "scte35SpliceInsert" in data:
        import capo_medialive.types.scte35_splice_insert

        out["scte35_splice_insert"] = (
            capo_medialive.types.scte35_splice_insert.deserialize_json(
                data["scte35SpliceInsert"]
            )
        )
    if "scte35TimeSignalApos" in data:
        import capo_medialive.types.scte35_time_signal_apos

        out["scte35_time_signal_apos"] = (
            capo_medialive.types.scte35_time_signal_apos.deserialize_json(
                data["scte35TimeSignalApos"]
            )
        )
    return out
