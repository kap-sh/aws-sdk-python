"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermItemAdditionalAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.match_rationale


class GlossaryTermItemAdditionalAttributes(TypedDict, closed=True):
    match_rationale: NotRequired[
        "aws_sdk_datazone.types.match_rationale.MatchRationale"
    ]
    """<p>List of rationales indicating why this item was matched by search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTermItemAdditionalAttributes) -> dict:
    out: dict = {}
    if "match_rationale" in value:
        import aws_sdk_datazone.types.match_rationale

        out["matchRationale"] = aws_sdk_datazone.types.match_rationale.serialize_json(
            value["match_rationale"]
        )
    return out


def deserialize_json(data: dict) -> GlossaryTermItemAdditionalAttributes:
    out: GlossaryTermItemAdditionalAttributes = {}  # type: ignore[typeddict-item]
    if "matchRationale" in data:
        import aws_sdk_datazone.types.match_rationale

        out["match_rationale"] = (
            aws_sdk_datazone.types.match_rationale.deserialize_json(
                data["matchRationale"]
            )
        )
    return out
