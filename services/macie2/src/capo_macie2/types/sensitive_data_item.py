"""Generated from Smithy shape ``com.amazonaws.macie2#SensitiveDataItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long
    import capo_macie2.types.default_detections
    import capo_macie2.types.sensitive_data_item_category


class SensitiveDataItem(TypedDict, closed=True):
    category: NotRequired[
        "capo_macie2.types.sensitive_data_item_category.SensitiveDataItemCategory"
    ]
    """<p>The category of sensitive data that was detected. For example: CREDENTIALS, for credentials data such as private keys or Amazon Web Services secret access keys; FINANCIAL_INFORMATION, for financial data such as credit card numbers; or, PERSONAL_INFORMATION, for personal health information, such as health insurance identification numbers, or personally identifiable information, such as passport numbers.</p>"""
    detections: NotRequired["capo_macie2.types.default_detections.DefaultDetections"]
    """<p>An array of objects, one for each type of sensitive data that was detected. Each object reports the number of occurrences of a specific type of sensitive data that was detected, and the location of up to 15 of those occurrences.</p>"""
    total_count: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of occurrences of the sensitive data that was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataItem) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_macie2.types.sensitive_data_item_category

        out["category"] = capo_macie2.types.sensitive_data_item_category.serialize_json(
            value["category"]
        )
    if "detections" in value:
        import capo_macie2.types.default_detections

        out["detections"] = capo_macie2.types.default_detections.serialize_json(
            value["detections"]
        )
    if "total_count" in value:
        out["totalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> SensitiveDataItem:
    out: SensitiveDataItem = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import capo_macie2.types.sensitive_data_item_category

        out["category"] = (
            capo_macie2.types.sensitive_data_item_category.deserialize_json(
                data["category"]
            )
        )
    if "detections" in data:
        import capo_macie2.types.default_detections

        out["detections"] = capo_macie2.types.default_detections.deserialize_json(
            data["detections"]
        )
    if "totalCount" in data:
        out["total_count"] = data["totalCount"]
    return out
