"""Generated from Smithy shape ``com.amazonaws.dlm#ArchiveRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.archive_retain_rule


class ArchiveRule(TypedDict):
    retain_rule: NotRequired["aws_sdk_dlm.types.archive_retain_rule.ArchiveRetainRule"]
    """<p>Information about the retention period for the snapshot archiving rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveRule) -> dict:
    out: dict = {}
    if "retain_rule" in value:
        import aws_sdk_dlm.types.archive_retain_rule

        out["RetainRule"] = aws_sdk_dlm.types.archive_retain_rule.serialize_json(
            value["retain_rule"]
        )
    return out


def deserialize_json(data: dict) -> ArchiveRule:
    out: ArchiveRule = {}  # type: ignore[typeddict-item]
    if "RetainRule" in data:
        import aws_sdk_dlm.types.archive_retain_rule

        out["retain_rule"] = aws_sdk_dlm.types.archive_retain_rule.deserialize_json(
            data["RetainRule"]
        )
    return out
