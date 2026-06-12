"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListTagOptionsFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_active
    import aws_sdk_service_catalog.types.tag_option_key
    import aws_sdk_service_catalog.types.tag_option_value


class ListTagOptionsFilters(TypedDict):
    key: NotRequired["aws_sdk_service_catalog.types.tag_option_key.TagOptionKey"]
    """<p>The TagOption key.</p>"""
    value: NotRequired["aws_sdk_service_catalog.types.tag_option_value.TagOptionValue"]
    """<p>The TagOption value.</p>"""
    active: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_active.TagOptionActive"
    ]
    """<p>The active state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagOptionsFilters) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "active" in value:
        out["Active"] = value["active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagOptionsFilters:
    out: ListTagOptionsFilters = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Active" in data:
        out["active"] = data["Active"]
    return out
