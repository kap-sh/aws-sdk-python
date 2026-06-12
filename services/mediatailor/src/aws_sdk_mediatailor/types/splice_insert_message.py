"""Generated from Smithy shape ``com.amazonaws.mediatailor#SpliceInsertMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer


class SpliceInsertMessage(TypedDict):
    avail_num: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>This is written to <code>splice_insert.avail_num</code>, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is <code>0</code>. Values must be between <code>0</code> and <code>256</code>, inclusive.</p>"""
    avails_expected: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>This is written to <code>splice_insert.avails_expected</code>, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is <code>0</code>. Values must be between <code>0</code> and <code>256</code>, inclusive.</p>"""
    splice_event_id: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>This is written to <code>splice_insert.splice_event_id</code>, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is <code>1</code>.</p>"""
    unique_program_id: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>This is written to <code>splice_insert.unique_program_id</code>, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is <code>0</code>. Values must be between <code>0</code> and <code>256</code>, inclusive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpliceInsertMessage) -> dict:
    out: dict = {}
    if "avail_num" in value:
        out["AvailNum"] = value["avail_num"]
    if "avails_expected" in value:
        out["AvailsExpected"] = value["avails_expected"]
    if "splice_event_id" in value:
        out["SpliceEventId"] = value["splice_event_id"]
    if "unique_program_id" in value:
        out["UniqueProgramId"] = value["unique_program_id"]
    return out


def deserialize_json(data: dict) -> SpliceInsertMessage:
    out: SpliceInsertMessage = {}  # type: ignore[typeddict-item]
    if "AvailNum" in data:
        out["avail_num"] = data["AvailNum"]
    if "AvailsExpected" in data:
        out["avails_expected"] = data["AvailsExpected"]
    if "SpliceEventId" in data:
        out["splice_event_id"] = data["SpliceEventId"]
    if "UniqueProgramId" in data:
        out["unique_program_id"] = data["UniqueProgramId"]
    return out
