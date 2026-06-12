"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#Categories``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.matched_categories
    import aws_sdk_connect_contact_lens.types.matched_details


class Categories(TypedDict):
    matched_categories: NotRequired[
        "aws_sdk_connect_contact_lens.types.matched_categories.MatchedCategories"
    ]
    """<p>The category rules that have been matched in the analyzed segment.</p>"""
    matched_details: NotRequired[
        "aws_sdk_connect_contact_lens.types.matched_details.MatchedDetails"
    ]
    """<p>The category rule that was matched and when it occurred in the transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Categories) -> dict:
    out: dict = {}
    if "matched_categories" in value:
        import aws_sdk_connect_contact_lens.types.matched_categories

        out["MatchedCategories"] = (
            aws_sdk_connect_contact_lens.types.matched_categories.serialize_json(
                value["matched_categories"]
            )
        )
    if "matched_details" in value:
        import aws_sdk_connect_contact_lens.types.matched_details

        out["MatchedDetails"] = (
            aws_sdk_connect_contact_lens.types.matched_details.serialize_json(
                value["matched_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Categories:
    out: Categories = {}  # type: ignore[typeddict-item]
    if "MatchedCategories" in data:
        import aws_sdk_connect_contact_lens.types.matched_categories

        out["matched_categories"] = (
            aws_sdk_connect_contact_lens.types.matched_categories.deserialize_json(
                data["MatchedCategories"]
            )
        )
    if "MatchedDetails" in data:
        import aws_sdk_connect_contact_lens.types.matched_details

        out["matched_details"] = (
            aws_sdk_connect_contact_lens.types.matched_details.deserialize_json(
                data["MatchedDetails"]
            )
        )
    return out
