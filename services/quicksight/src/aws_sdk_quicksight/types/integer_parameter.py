"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.sensitive_long_list


class IntegerParameter(TypedDict):
    name: "aws_sdk_quicksight.types.non_empty_string.NonEmptyString"
    """<p>The name of the integer parameter.</p>"""
    values: "aws_sdk_quicksight.types.sensitive_long_list.SensitiveLongList"
    """<p>The values for the integer parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.sensitive_long_list

    out["Values"] = aws_sdk_quicksight.types.sensitive_long_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> IntegerParameter:
    out: IntegerParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("IntegerParameter.name required")
    if "Values" in data:
        import aws_sdk_quicksight.types.sensitive_long_list

        out["values"] = aws_sdk_quicksight.types.sensitive_long_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("IntegerParameter.values required")
    return out
