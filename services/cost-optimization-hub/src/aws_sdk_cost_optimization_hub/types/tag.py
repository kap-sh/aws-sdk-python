"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Tag``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Tag(TypedDict):
    key: NotRequired["str"]
    """<p>The key that's associated with the tag.</p>"""
    value: NotRequired["str"]
    """<p>The value that's associated with the tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
