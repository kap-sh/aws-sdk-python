"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageSortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_sort_key
    import aws_sdk_guardduty.types.order_by


class CoverageSortCriteria(TypedDict, closed=True):
    attribute_name: NotRequired[
        "aws_sdk_guardduty.types.coverage_sort_key.CoverageSortKey"
    ]
    """<p>Represents the field name used to sort the coverage details.</p> <note> <p>Replace the enum value <code>CLUSTER_NAME</code> with <code>EKS_CLUSTER_NAME</code>. <code>CLUSTER_NAME</code> has been deprecated.</p> </note>"""
    order_by: NotRequired["aws_sdk_guardduty.types.order_by.OrderBy"]
    """<p>The order in which the sorted findings are to be displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageSortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        import aws_sdk_guardduty.types.coverage_sort_key

        out["attributeName"] = aws_sdk_guardduty.types.coverage_sort_key.serialize_json(
            value["attribute_name"]
        )
    if "order_by" in value:
        import aws_sdk_guardduty.types.order_by

        out["orderBy"] = aws_sdk_guardduty.types.order_by.serialize_json(
            value["order_by"]
        )
    return out


def deserialize_json(data: dict) -> CoverageSortCriteria:
    out: CoverageSortCriteria = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        import aws_sdk_guardduty.types.coverage_sort_key

        out["attribute_name"] = (
            aws_sdk_guardduty.types.coverage_sort_key.deserialize_json(
                data["attributeName"]
            )
        )
    if "orderBy" in data:
        import aws_sdk_guardduty.types.order_by

        out["order_by"] = aws_sdk_guardduty.types.order_by.deserialize_json(
            data["orderBy"]
        )
    return out
