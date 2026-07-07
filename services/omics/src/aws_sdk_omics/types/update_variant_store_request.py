"""Generated from Smithy shape ``com.amazonaws.omics#UpdateVariantStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.description


class UpdateVariantStoreRequest(TypedDict, closed=True):
    name: "str"
    """<p>A name for the store.</p>"""
    description: NotRequired["aws_sdk_omics.types.description.Description"]
    """<p>A description for the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVariantStoreRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateVariantStoreRequest:
    out: UpdateVariantStoreRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
