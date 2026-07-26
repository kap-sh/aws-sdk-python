"""Generated from Smithy shape ``com.amazonaws.dlm#ArchiveRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.archive_retain_rule


class ArchiveRule(TypedDict, closed=True):
    retain_rule: NotRequired["capo_dlm.types.archive_retain_rule.ArchiveRetainRule"]
    """<p>Information about the retention period for the snapshot archiving rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveRule) -> dict:
    out: dict = {}
    if "retain_rule" in value:
        import capo_dlm.types.archive_retain_rule

        out["RetainRule"] = capo_dlm.types.archive_retain_rule.serialize_json(
            value["retain_rule"]
        )
    return out


def deserialize_json(data: dict) -> ArchiveRule:
    out: ArchiveRule = {}  # type: ignore[typeddict-item]
    if "RetainRule" in data:
        import capo_dlm.types.archive_retain_rule

        out["retain_rule"] = capo_dlm.types.archive_retain_rule.deserialize_json(
            data["RetainRule"]
        )
    return out
