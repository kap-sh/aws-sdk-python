"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.sensitive_double_list


class DecimalParameter(TypedDict, closed=True):
    name: "aws_sdk_quicksight.types.non_empty_string.NonEmptyString"
    """<p>A display name for the decimal parameter.</p>"""
    values: "aws_sdk_quicksight.types.sensitive_double_list.SensitiveDoubleList"
    """<p>The values for the decimal parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.sensitive_double_list

    out["Values"] = aws_sdk_quicksight.types.sensitive_double_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> DecimalParameter:
    out: DecimalParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DecimalParameter.name required")
    if "Values" in data:
        import aws_sdk_quicksight.types.sensitive_double_list

        out["values"] = aws_sdk_quicksight.types.sensitive_double_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("DecimalParameter.values required")
    return out
