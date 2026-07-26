"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CatalogItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attributes
    import capo_customer_profiles.types.sensitive_string1_to255
    import capo_customer_profiles.types.sensitive_string1_to1000
    import capo_customer_profiles.types.timestamp


class CatalogItem(TypedDict, closed=True):
    id: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The unique identifier for the catalog item.</p>"""
    name: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The display name of the catalog item.</p>"""
    code: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The product code or SKU of the catalog item.</p>"""
    type: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The type classification of the catalog item.</p>"""
    category: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The category to which the catalog item belongs.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>A detailed description of the catalog item.</p>"""
    additional_information: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>Supplementary information about the catalog item beyond the basic description.</p>"""
    image_link: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>The URL link to the item's image.</p>"""
    link: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>The URL link to the item's detailed page or external resource.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the catalog item was created.</p>"""
    updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the catalog item was last updated.</p>"""
    price: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The price of the catalog item.</p>"""
    attributes: NotRequired["capo_customer_profiles.types.attributes.Attributes"]
    """<p>Additional attributes or properties associated with the catalog item stored as key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "code" in value:
        out["Code"] = value["code"]
    if "type" in value:
        out["Type"] = value["type"]
    if "category" in value:
        out["Category"] = value["category"]
    if "description" in value:
        out["Description"] = value["description"]
    if "additional_information" in value:
        out["AdditionalInformation"] = value["additional_information"]
    if "image_link" in value:
        out["ImageLink"] = value["image_link"]
    if "link" in value:
        out["Link"] = value["link"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["UpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "price" in value:
        out["Price"] = value["price"]
    if "attributes" in value:
        import capo_customer_profiles.types.attributes

        out["Attributes"] = capo_customer_profiles.types.attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> CatalogItem:
    out: CatalogItem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Category" in data:
        out["category"] = data["Category"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AdditionalInformation" in data:
        out["additional_information"] = data["AdditionalInformation"]
    if "ImageLink" in data:
        out["image_link"] = data["ImageLink"]
    if "Link" in data:
        out["link"] = data["Link"]
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["updated_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "Price" in data:
        out["price"] = data["Price"]
    if "Attributes" in data:
        import capo_customer_profiles.types.attributes

        out["attributes"] = capo_customer_profiles.types.attributes.deserialize_json(
            data["Attributes"]
        )
    return out
