"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductLastModifiedDateFilterDateRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.date_time_iso8601


class ContainerProductLastModifiedDateFilterDateRange(TypedDict, closed=True):
    after_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>Date after which the container product was last modified.</p>"""
    before_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>Date before which the container product was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductLastModifiedDateFilterDateRange) -> dict:
    out: dict = {}
    if "after_value" in value:
        out["AfterValue"] = value["after_value"]
    if "before_value" in value:
        out["BeforeValue"] = value["before_value"]
    return out


def deserialize_json(data: dict) -> ContainerProductLastModifiedDateFilterDateRange:
    out: ContainerProductLastModifiedDateFilterDateRange = {}  # type: ignore[typeddict-item]
    if "AfterValue" in data:
        out["after_value"] = data["AfterValue"]
    if "BeforeValue" in data:
        out["before_value"] = data["BeforeValue"]
    return out
