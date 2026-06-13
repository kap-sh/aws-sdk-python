"""Generated from Smithy shape ``com.amazonaws.omics#VcfOptions``."""

from typing import TypedDict

from typing_extensions import NotRequired


class VcfOptions(TypedDict):
    ignore_qual_field: NotRequired["bool"]
    """<p>The file's ignore qual field setting.</p>"""
    ignore_filter_field: NotRequired["bool"]
    """<p>The file's ignore filter field setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VcfOptions) -> dict:
    out: dict = {}
    if "ignore_qual_field" in value:
        out["ignoreQualField"] = value["ignore_qual_field"]
    if "ignore_filter_field" in value:
        out["ignoreFilterField"] = value["ignore_filter_field"]
    return out


def deserialize_json(data: dict) -> VcfOptions:
    out: VcfOptions = {}  # type: ignore[typeddict-item]
    if "ignoreQualField" in data:
        out["ignore_qual_field"] = data["ignoreQualField"]
    if "ignoreFilterField" in data:
        out["ignore_filter_field"] = data["ignoreFilterField"]
    return out
