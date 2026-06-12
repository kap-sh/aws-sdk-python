"""Generated from Smithy shape ``com.amazonaws.macie2#TagCriterionPairForJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class TagCriterionPairForJob(TypedDict):
    key: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The value for the tag key to use in the condition.</p>"""
    value: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The tag value to use in the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagCriterionPairForJob) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagCriterionPairForJob:
    out: TagCriterionPairForJob = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
