"""Generated from Smithy shape ``com.amazonaws.guardduty#SortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.order_by
    import aws_sdk_guardduty.types.string


class SortCriteria(TypedDict, closed=True):
    attribute_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Represents the finding attribute, such as <code>accountId</code>, that sorts the findings.</p>"""
    order_by: NotRequired["aws_sdk_guardduty.types.order_by.OrderBy"]
    """<p>The order by which the sorted findings are to be displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["attributeName"] = value["attribute_name"]
    if "order_by" in value:
        import aws_sdk_guardduty.types.order_by

        out["orderBy"] = aws_sdk_guardduty.types.order_by.serialize_json(
            value["order_by"]
        )
    return out


def deserialize_json(data: dict) -> SortCriteria:
    out: SortCriteria = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        out["attribute_name"] = data["attributeName"]
    if "orderBy" in data:
        import aws_sdk_guardduty.types.order_by

        out["order_by"] = aws_sdk_guardduty.types.order_by.deserialize_json(
            data["orderBy"]
        )
    return out
