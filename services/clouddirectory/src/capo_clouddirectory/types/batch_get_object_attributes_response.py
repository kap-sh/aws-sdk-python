"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchGetObjectAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_key_and_value_list


class BatchGetObjectAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>The attribute values that are associated with an object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetObjectAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["Attributes"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetObjectAttributesResponse:
    out: BatchGetObjectAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["attributes"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["Attributes"]
            )
        )
    return out
