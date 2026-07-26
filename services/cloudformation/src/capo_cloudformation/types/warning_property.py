"""Generated from Smithy shape ``com.amazonaws.cloudformation#WarningProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.property_description
    import capo_cloudformation.types.property_path
    import capo_cloudformation.types.required_property


class WarningProperty(TypedDict, closed=True):
    property_path: NotRequired["capo_cloudformation.types.property_path.PropertyPath"]
    """<p>The path of the property. For example, if this is for the <code>S3Bucket</code> member of the <code>Code</code> property, the property path would be <code>Code/S3Bucket</code>.</p>"""
    required: NotRequired[
        "capo_cloudformation.types.required_property.RequiredProperty"
    ]
    """<p>If <code>true</code>, the specified property is required.</p>"""
    description: NotRequired[
        "capo_cloudformation.types.property_description.PropertyDescription"
    ]
    """<p>The description of the property from the resource provider schema.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: WarningProperty, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "property_path" in value:
        pairs.append((f"{prefix}.PropertyPath", str(value["property_path"])))
    if "required" in value:
        pairs.append((f"{prefix}.Required", "true" if value["required"] else "false"))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> WarningProperty:
    out: WarningProperty = {}  # type: ignore[typeddict-item]
    child_property_path = el.find("PropertyPath")
    if child_property_path is not None:
        out["property_path"] = str(child_property_path.text or "")
    child_required = el.find("Required")
    if child_required is not None:
        out["required"] = (child_required.text or "").lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
