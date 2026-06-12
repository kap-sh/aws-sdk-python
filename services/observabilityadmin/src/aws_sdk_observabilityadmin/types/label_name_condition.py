"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LabelNameCondition``."""

from typing import TypedDict

from typing_extensions import NotRequired


class LabelNameCondition(TypedDict):
    label_name: NotRequired["str"]
    """<p> The label name to match, supporting alphanumeric characters, underscores, hyphens, and colons. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LabelNameCondition) -> dict:
    out: dict = {}
    if "label_name" in value:
        out["LabelName"] = value["label_name"]
    return out


def deserialize_json(data: dict) -> LabelNameCondition:
    out: LabelNameCondition = {}  # type: ignore[typeddict-item]
    if "LabelName" in data:
        out["label_name"] = data["LabelName"]
    return out
