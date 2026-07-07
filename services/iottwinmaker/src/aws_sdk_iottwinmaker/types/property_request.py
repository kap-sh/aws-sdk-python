"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.property_definition_request
    import aws_sdk_iottwinmaker.types.property_update_type


class PropertyRequest(TypedDict, closed=True):
    definition: NotRequired[
        "aws_sdk_iottwinmaker.types.property_definition_request.PropertyDefinitionRequest"
    ]
    """<p>An object that specifies information about a property.</p>"""
    value: NotRequired["aws_sdk_iottwinmaker.types.data_value.DataValue"]
    """<p>The value of the property.</p>"""
    update_type: NotRequired[
        "aws_sdk_iottwinmaker.types.property_update_type.PropertyUpdateType"
    ]
    """<p>The update type of the update property request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyRequest) -> dict:
    out: dict = {}
    if "definition" in value:
        import aws_sdk_iottwinmaker.types.property_definition_request

        out["definition"] = (
            aws_sdk_iottwinmaker.types.property_definition_request.serialize_json(
                value["definition"]
            )
        )
    if "value" in value:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.serialize_json(
            value["value"]
        )
    if "update_type" in value:
        out["updateType"] = value["update_type"]
    return out


def deserialize_json(data: dict) -> PropertyRequest:
    out: PropertyRequest = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import aws_sdk_iottwinmaker.types.property_definition_request

        out["definition"] = (
            aws_sdk_iottwinmaker.types.property_definition_request.deserialize_json(
                data["definition"]
            )
        )
    if "value" in data:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    if "updateType" in data:
        out["update_type"] = data["updateType"]
    return out
