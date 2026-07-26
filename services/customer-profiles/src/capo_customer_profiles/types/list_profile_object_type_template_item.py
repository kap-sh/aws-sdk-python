"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypeTemplateItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class ListProfileObjectTypeTemplateItem(TypedDict, closed=True):
    template_id: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>A unique identifier for the object template.</p>"""
    source_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the source of the object template.</p>"""
    source_object: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The source of the object template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypeTemplateItem) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_object" in value:
        out["SourceObject"] = value["source_object"]
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypeTemplateItem:
    out: ListProfileObjectTypeTemplateItem = {}  # type: ignore[typeddict-item]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    if "SourceObject" in data:
        out["source_object"] = data["SourceObject"]
    return out
