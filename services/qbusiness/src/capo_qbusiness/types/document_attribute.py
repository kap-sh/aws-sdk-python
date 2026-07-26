"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_key
    import capo_qbusiness.types.document_attribute_value


class DocumentAttribute(TypedDict, closed=True):
    name: "capo_qbusiness.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier for the attribute.</p>"""
    value: "capo_qbusiness.types.document_attribute_value.DocumentAttributeValue"
    """<p>The value of the attribute. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttribute) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_qbusiness.types.document_attribute_value

    out["value"] = capo_qbusiness.types.document_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> DocumentAttribute:
    out: DocumentAttribute = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DocumentAttribute.name required")
    if "value" in data:
        import capo_qbusiness.types.document_attribute_value

        out["value"] = capo_qbusiness.types.document_attribute_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("DocumentAttribute.value required")
    return out
