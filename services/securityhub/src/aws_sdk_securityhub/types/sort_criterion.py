"""Generated from Smithy shape ``com.amazonaws.securityhub#SortCriterion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.sort_order


class SortCriterion(TypedDict):
    field: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The finding attribute used to sort findings.</p>"""
    sort_order: NotRequired["aws_sdk_securityhub.types.sort_order.SortOrder"]
    """<p>The order used to sort findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriterion) -> dict:
    out: dict = {}
    if "field" in value:
        out["Field"] = value["field"]
    if "sort_order" in value:
        import aws_sdk_securityhub.types.sort_order

        out["SortOrder"] = aws_sdk_securityhub.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> SortCriterion:
    out: SortCriterion = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        out["field"] = data["Field"]
    if "SortOrder" in data:
        import aws_sdk_securityhub.types.sort_order

        out["sort_order"] = aws_sdk_securityhub.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    return out
