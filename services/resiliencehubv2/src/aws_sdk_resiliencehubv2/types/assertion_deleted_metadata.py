"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssertionDeletedMetadata``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AssertionDeletedMetadata(TypedDict):
    assertion_id: NotRequired["str"]
    """<p>The unique identifier of the deleted assertion.</p>"""
    assertion_name: NotRequired["str"]
    """<p>The name of the deleted assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssertionDeletedMetadata) -> dict:
    out: dict = {}
    if "assertion_id" in value:
        out["assertionId"] = value["assertion_id"]
    if "assertion_name" in value:
        out["assertionName"] = value["assertion_name"]
    return out


def deserialize_json(data: dict) -> AssertionDeletedMetadata:
    out: AssertionDeletedMetadata = {}  # type: ignore[typeddict-item]
    if "assertionId" in data:
        out["assertion_id"] = data["assertionId"]
    if "assertionName" in data:
        out["assertion_name"] = data["assertionName"]
    return out
