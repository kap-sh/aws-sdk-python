"""Generated from Smithy shape ``com.amazonaws.macie2#BucketSortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.order_by


class BucketSortCriteria(TypedDict, closed=True):
    attribute_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the bucket property to sort the results by. This value can be one of the following properties that Amazon Macie defines as bucket metadata: accountId, bucketName, classifiableObjectCount, classifiableSizeInBytes, objectCount, sensitivityScore, or sizeInBytes.</p>"""
    order_by: NotRequired["aws_sdk_macie2.types.order_by.OrderBy"]
    """<p>The sort order to apply to the results, based on the value specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketSortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["attributeName"] = value["attribute_name"]
    if "order_by" in value:
        import aws_sdk_macie2.types.order_by

        out["orderBy"] = aws_sdk_macie2.types.order_by.serialize_json(value["order_by"])
    return out


def deserialize_json(data: dict) -> BucketSortCriteria:
    out: BucketSortCriteria = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        out["attribute_name"] = data["attributeName"]
    if "orderBy" in data:
        import aws_sdk_macie2.types.order_by

        out["order_by"] = aws_sdk_macie2.types.order_by.deserialize_json(
            data["orderBy"]
        )
    return out
