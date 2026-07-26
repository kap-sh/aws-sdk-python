"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id


class DescribeExportRequest(TypedDict, closed=True):
    export_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the export to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeExportRequest:
    out: DescribeExportRequest = {}  # type: ignore[typeddict-item]
    return out
