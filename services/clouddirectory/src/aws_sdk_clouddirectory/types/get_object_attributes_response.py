"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetObjectAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list


class GetObjectAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>The attributes that are associated with the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["Attributes"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetObjectAttributesResponse:
    out: GetObjectAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["attributes"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["Attributes"]
            )
        )
    return out
