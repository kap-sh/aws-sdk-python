"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductListingItemAdditionalAttributes``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.forms
    import aws_sdk_datazone.types.match_rationale


class DataProductListingItemAdditionalAttributes(TypedDict):
    forms: NotRequired["aws_sdk_datazone.types.forms.Forms"]
    """<p>The metadata forms of the asset of the data product. </p>"""
    match_rationale: NotRequired[
        "aws_sdk_datazone.types.match_rationale.MatchRationale"
    ]
    """<p>List of rationales indicating why this item was matched by search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductListingItemAdditionalAttributes) -> dict:
    out: dict = {}
    if "forms" in value:
        out["forms"] = value["forms"]
    if "match_rationale" in value:
        import aws_sdk_datazone.types.match_rationale

        out["matchRationale"] = aws_sdk_datazone.types.match_rationale.serialize_json(
            value["match_rationale"]
        )
    return out


def deserialize_json(data: dict) -> DataProductListingItemAdditionalAttributes:
    out: DataProductListingItemAdditionalAttributes = {}  # type: ignore[typeddict-item]
    if "forms" in data:
        out["forms"] = data["forms"]
    if "matchRationale" in data:
        import aws_sdk_datazone.types.match_rationale

        out["match_rationale"] = (
            aws_sdk_datazone.types.match_rationale.deserialize_json(
                data["matchRationale"]
            )
        )
    return out
