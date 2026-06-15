"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SearchStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.long
    import aws_sdk_cloudsearch_domain.types.string


class SearchStatus(TypedDict):
    timems: "aws_sdk_cloudsearch_domain.types.long.Long"
    """<p>How long it took to process the request, in milliseconds.</p>"""
    rid: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The encrypted resource ID for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchStatus) -> dict:
    out: dict = {}
    out["timems"] = value.get("timems", 0)
    if "rid" in value:
        out["rid"] = value["rid"]
    return out


def deserialize_json(data: dict) -> SearchStatus:
    out: SearchStatus = {}  # type: ignore[typeddict-item]
    if "timems" in data:
        out["timems"] = data["timems"]
    else:
        out["timems"] = 0
    if "rid" in data:
        out["rid"] = data["rid"]
    return out
