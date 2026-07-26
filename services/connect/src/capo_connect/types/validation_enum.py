"""Generated from Smithy shape ``com.amazonaws.connect#ValidationEnum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.validation_enum_values


class ValidationEnum(TypedDict, closed=True):
    strict: "capo_connect.types.boolean.Boolean"
    """<p>Boolean that defaults to false. When true, only values specified in the enum list are allowed. When false, custom values beyond the enumerated list are permitted.</p>"""
    values: NotRequired[
        "capo_connect.types.validation_enum_values.ValidationEnumValues"
    ]
    """<p>A list of predefined values that are allowed for this attribute. These values are always permitted regardless of the Strict setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationEnum) -> dict:
    out: dict = {}
    out["Strict"] = value.get("strict", False)
    if "values" in value:
        import capo_connect.types.validation_enum_values

        out["Values"] = capo_connect.types.validation_enum_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> ValidationEnum:
    out: ValidationEnum = {}  # type: ignore[typeddict-item]
    if "Strict" in data:
        out["strict"] = data["Strict"]
    else:
        out["strict"] = False
    if "Values" in data:
        import capo_connect.types.validation_enum_values

        out["values"] = capo_connect.types.validation_enum_values.deserialize_json(
            data["Values"]
        )
    return out
