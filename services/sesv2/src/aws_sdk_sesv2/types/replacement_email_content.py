"""Generated from Smithy shape ``com.amazonaws.sesv2#ReplacementEmailContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.replacement_template


class ReplacementEmailContent(TypedDict):
    replacement_template: NotRequired[
        "aws_sdk_sesv2.types.replacement_template.ReplacementTemplate"
    ]
    """<p>The <code>ReplacementTemplate</code> associated with <code>ReplacementEmailContent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacementEmailContent) -> dict:
    out: dict = {}
    if "replacement_template" in value:
        import aws_sdk_sesv2.types.replacement_template

        out["ReplacementTemplate"] = (
            aws_sdk_sesv2.types.replacement_template.serialize_json(
                value["replacement_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplacementEmailContent:
    out: ReplacementEmailContent = {}  # type: ignore[typeddict-item]
    if "ReplacementTemplate" in data:
        import aws_sdk_sesv2.types.replacement_template

        out["replacement_template"] = (
            aws_sdk_sesv2.types.replacement_template.deserialize_json(
                data["ReplacementTemplate"]
            )
        )
    return out
