"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetLinkAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_key_and_value_list


class GetLinkAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>The attributes that are associated with the typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["Attributes"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLinkAttributesResponse:
    out: GetLinkAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["attributes"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["Attributes"]
            )
        )
    return out
