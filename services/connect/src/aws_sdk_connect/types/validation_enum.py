"""Generated from Smithy shape ``com.amazonaws.connect#ValidationEnum``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.validation_enum_values


class ValidationEnum(TypedDict):
    strict: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Boolean that defaults to false. When true, only values specified in the enum list are allowed. When false, custom values beyond the enumerated list are permitted.</p>"""
    values: NotRequired[
        "aws_sdk_connect.types.validation_enum_values.ValidationEnumValues"
    ]
    """<p>A list of predefined values that are allowed for this attribute. These values are always permitted regardless of the Strict setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationEnum) -> dict:
    out: dict = {}
    out["Strict"] = value.get("strict", False)
    if "values" in value:
        import aws_sdk_connect.types.validation_enum_values

        out["Values"] = aws_sdk_connect.types.validation_enum_values.serialize_json(
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
        import aws_sdk_connect.types.validation_enum_values

        out["values"] = aws_sdk_connect.types.validation_enum_values.deserialize_json(
            data["Values"]
        )
    return out
