"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssertionUpdatedMetadata``."""

from typing_extensions import NotRequired, TypedDict


class AssertionUpdatedMetadata(TypedDict, closed=True):
    assertion_id: NotRequired["str"]
    """<p>The unique identifier of the updated assertion.</p>"""
    assertion_name: NotRequired["str"]
    """<p>The name of the updated assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssertionUpdatedMetadata) -> dict:
    out: dict = {}
    if "assertion_id" in value:
        out["assertionId"] = value["assertion_id"]
    if "assertion_name" in value:
        out["assertionName"] = value["assertion_name"]
    return out


def deserialize_json(data: dict) -> AssertionUpdatedMetadata:
    out: AssertionUpdatedMetadata = {}  # type: ignore[typeddict-item]
    if "assertionId" in data:
        out["assertion_id"] = data["assertionId"]
    if "assertionName" in data:
        out["assertion_name"] = data["assertionName"]
    return out
