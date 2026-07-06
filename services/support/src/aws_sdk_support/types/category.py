"""Generated from Smithy shape ``com.amazonaws.support#Category``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.category_code
    import aws_sdk_support.types.category_name


class Category(TypedDict, closed=True):
    code: NotRequired["aws_sdk_support.types.category_code.CategoryCode"]
    """<p>The category code for the support case.</p>"""
    name: NotRequired["aws_sdk_support.types.category_name.CategoryName"]
    """<p>The category name for the support case.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Category) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "name" in data:
        out["name"] = data["name"]
    return out
