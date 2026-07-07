"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyValueHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.entity_property_reference
    import aws_sdk_iottwinmaker.types.values


class PropertyValueHistory(TypedDict, closed=True):
    entity_property_reference: (
        "aws_sdk_iottwinmaker.types.entity_property_reference.EntityPropertyReference"
    )
    """<p>An object that uniquely identifies an entity property.</p>"""
    values: NotRequired["aws_sdk_iottwinmaker.types.values.Values"]
    """<p>A list of objects that contain information about the values in the history of a time series property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValueHistory) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.entity_property_reference

    out["entityPropertyReference"] = (
        aws_sdk_iottwinmaker.types.entity_property_reference.serialize_json(
            value["entity_property_reference"]
        )
    )
    if "values" in value:
        import aws_sdk_iottwinmaker.types.values

        out["values"] = aws_sdk_iottwinmaker.types.values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> PropertyValueHistory:
    out: PropertyValueHistory = {}  # type: ignore[typeddict-item]
    if "entityPropertyReference" in data:
        import aws_sdk_iottwinmaker.types.entity_property_reference

        out["entity_property_reference"] = (
            aws_sdk_iottwinmaker.types.entity_property_reference.deserialize_json(
                data["entityPropertyReference"]
            )
        )
    else:
        raise DeserializationError(
            "PropertyValueHistory.entity_property_reference required"
        )
    if "values" in data:
        import aws_sdk_iottwinmaker.types.values

        out["values"] = aws_sdk_iottwinmaker.types.values.deserialize_json(
            data["values"]
        )
    return out
