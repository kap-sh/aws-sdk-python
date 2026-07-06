"""Generated from Smithy shape ``com.amazonaws.qapps#CategoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.uuid


class CategoryInput(TypedDict, closed=True):
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the category.</p>"""
    title: "str"
    """<p>The name of the category.</p>"""
    color: NotRequired["str"]
    """<p>The color of the category, represented as a hexadecimal value of either 3 or 6 digits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    if "color" in value:
        out["color"] = value["color"]
    return out


def deserialize_json(data: dict) -> CategoryInput:
    out: CategoryInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CategoryInput.id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CategoryInput.title required")
    if "color" in data:
        out["color"] = data["color"]
    return out
