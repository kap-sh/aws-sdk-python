"""Generated from Smithy shape ``com.amazonaws.inspector2#SortCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.sort_field
    import aws_sdk_inspector2.types.sort_order


class SortCriteria(TypedDict):
    field: "aws_sdk_inspector2.types.sort_field.SortField"
    """<p>The finding detail field by which results are sorted.</p>"""
    sort_order: "aws_sdk_inspector2.types.sort_order.SortOrder"
    """<p>The order by which findings are sorted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> SortCriteria:
    out: SortCriteria = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    else:
        raise DeserializationError("SortCriteria.field required")
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    else:
        raise DeserializationError("SortCriteria.sort_order required")
    return out
