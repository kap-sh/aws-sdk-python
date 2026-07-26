"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string
    import capo_guardduty.types.total


class UsageResourceResult(TypedDict, closed=True):
    resource: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services resource that generated usage.</p>"""
    total: NotRequired["capo_guardduty.types.total.Total"]
    """<p>Represents the sum total of usage for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageResourceResult) -> dict:
    out: dict = {}
    if "resource" in value:
        out["resource"] = value["resource"]
    if "total" in value:
        import capo_guardduty.types.total

        out["total"] = capo_guardduty.types.total.serialize_json(value["total"])
    return out


def deserialize_json(data: dict) -> UsageResourceResult:
    out: UsageResourceResult = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "total" in data:
        import capo_guardduty.types.total

        out["total"] = capo_guardduty.types.total.deserialize_json(data["total"])
    return out
