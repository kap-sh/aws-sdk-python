"""Generated from Smithy shape ``com.amazonaws.pinpoint#AttributesResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of__string


class AttributesResource(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application.</p>"""
    attribute_type: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of attribute or attributes that were removed from the endpoints. Valid values are:</p> <ul><li><p>endpoint-custom-attributes - Custom attributes that describe endpoints.</p></li> <li><p>endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints.</p></li> <li><p>endpoint-user-attributes - Custom attributes that describe users.</p></li></ul>"""
    attributes: NotRequired["capo_pinpoint.types.list_of__string.ListOf__string"]
    """<p>An array that specifies the names of the attributes that were removed from the endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributesResource) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "attribute_type" in value:
        out["AttributeType"] = value["attribute_type"]
    if "attributes" in value:
        import capo_pinpoint.types.list_of__string

        out["Attributes"] = capo_pinpoint.types.list_of__string.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> AttributesResource:
    out: AttributesResource = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "AttributeType" in data:
        out["attribute_type"] = data["AttributeType"]
    if "Attributes" in data:
        import capo_pinpoint.types.list_of__string

        out["attributes"] = capo_pinpoint.types.list_of__string.deserialize_json(
            data["Attributes"]
        )
    return out
