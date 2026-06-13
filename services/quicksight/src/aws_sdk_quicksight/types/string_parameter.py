"""Generated from Smithy shape ``com.amazonaws.quicksight#StringParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.sensitive_string_list


class StringParameter(TypedDict):
    name: "aws_sdk_quicksight.types.non_empty_string.NonEmptyString"
    """<p>A display name for a string parameter.</p>"""
    values: "aws_sdk_quicksight.types.sensitive_string_list.SensitiveStringList"
    """<p>The values of a string parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.sensitive_string_list

    out["Values"] = aws_sdk_quicksight.types.sensitive_string_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> StringParameter:
    out: StringParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StringParameter.name required")
    if "Values" in data:
        import aws_sdk_quicksight.types.sensitive_string_list

        out["values"] = aws_sdk_quicksight.types.sensitive_string_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("StringParameter.values required")
    return out
