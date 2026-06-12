"""Generated from Smithy shape ``com.amazonaws.translate#Term``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.string


class Term(TypedDict):
    source_text: NotRequired["aws_sdk_translate.types.string.String"]
    """<p>The source text of the term being translated by the custom terminology.</p>"""
    target_text: NotRequired["aws_sdk_translate.types.string.String"]
    """<p>The target text of the term being translated by the custom terminology.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Term) -> dict:
    out: dict = {}
    if "source_text" in value:
        out["SourceText"] = value["source_text"]
    if "target_text" in value:
        out["TargetText"] = value["target_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Term:
    out: Term = {}  # type: ignore[typeddict-item]
    if "SourceText" in data:
        out["source_text"] = data["SourceText"]
    if "TargetText" in data:
        out["target_text"] = data["TargetText"]
    return out
