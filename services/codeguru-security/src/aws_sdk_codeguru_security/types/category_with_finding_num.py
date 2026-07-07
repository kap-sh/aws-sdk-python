"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CategoryWithFindingNum``."""

from typing_extensions import NotRequired, TypedDict


class CategoryWithFindingNum(TypedDict, closed=True):
    category_name: NotRequired["str"]
    """<p>The name of the finding category. A finding category is determined by the detector that detected the finding.</p>"""
    finding_number: NotRequired["int"]
    """<p>The number of open findings in the category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryWithFindingNum) -> dict:
    out: dict = {}
    if "category_name" in value:
        out["categoryName"] = value["category_name"]
    if "finding_number" in value:
        out["findingNumber"] = value["finding_number"]
    return out


def deserialize_json(data: dict) -> CategoryWithFindingNum:
    out: CategoryWithFindingNum = {}  # type: ignore[typeddict-item]
    if "categoryName" in data:
        out["category_name"] = data["categoryName"]
    if "findingNumber" in data:
        out["finding_number"] = data["findingNumber"]
    return out
