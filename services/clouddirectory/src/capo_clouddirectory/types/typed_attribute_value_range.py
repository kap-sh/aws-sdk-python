"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedAttributeValueRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.range_mode
    import capo_clouddirectory.types.typed_attribute_value


class TypedAttributeValueRange(TypedDict, closed=True):
    start_mode: "capo_clouddirectory.types.range_mode.RangeMode"
    """<p>The inclusive or exclusive range start.</p>"""
    start_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The value to start the range at.</p>"""
    end_mode: "capo_clouddirectory.types.range_mode.RangeMode"
    """<p>The inclusive or exclusive range end.</p>"""
    end_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The attribute value to terminate the range at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedAttributeValueRange) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.range_mode

    out["StartMode"] = capo_clouddirectory.types.range_mode.serialize_json(
        value["start_mode"]
    )
    if "start_value" in value:
        import capo_clouddirectory.types.typed_attribute_value

        out["StartValue"] = (
            capo_clouddirectory.types.typed_attribute_value.serialize_json(
                value["start_value"]
            )
        )
    import capo_clouddirectory.types.range_mode

    out["EndMode"] = capo_clouddirectory.types.range_mode.serialize_json(
        value["end_mode"]
    )
    if "end_value" in value:
        import capo_clouddirectory.types.typed_attribute_value

        out["EndValue"] = (
            capo_clouddirectory.types.typed_attribute_value.serialize_json(
                value["end_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> TypedAttributeValueRange:
    out: TypedAttributeValueRange = {}  # type: ignore[typeddict-item]
    if "StartMode" in data:
        import capo_clouddirectory.types.range_mode

        out["start_mode"] = capo_clouddirectory.types.range_mode.deserialize_json(
            data["StartMode"]
        )
    else:
        raise DeserializationError("TypedAttributeValueRange.start_mode required")
    if "StartValue" in data:
        import capo_clouddirectory.types.typed_attribute_value

        out["start_value"] = (
            capo_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["StartValue"]
            )
        )
    if "EndMode" in data:
        import capo_clouddirectory.types.range_mode

        out["end_mode"] = capo_clouddirectory.types.range_mode.deserialize_json(
            data["EndMode"]
        )
    else:
        raise DeserializationError("TypedAttributeValueRange.end_mode required")
    if "EndValue" in data:
        import capo_clouddirectory.types.typed_attribute_value

        out["end_value"] = (
            capo_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["EndValue"]
            )
        )
    return out
