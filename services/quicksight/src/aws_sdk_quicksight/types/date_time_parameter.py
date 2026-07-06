"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.sensitive_timestamp_list


class DateTimeParameter(TypedDict, closed=True):
    name: "aws_sdk_quicksight.types.non_empty_string.NonEmptyString"
    """<p>A display name for the date-time parameter.</p>"""
    values: "aws_sdk_quicksight.types.sensitive_timestamp_list.SensitiveTimestampList"
    """<p>The values for the date-time parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.sensitive_timestamp_list

    out["Values"] = aws_sdk_quicksight.types.sensitive_timestamp_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> DateTimeParameter:
    out: DateTimeParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DateTimeParameter.name required")
    if "Values" in data:
        import aws_sdk_quicksight.types.sensitive_timestamp_list

        out["values"] = (
            aws_sdk_quicksight.types.sensitive_timestamp_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("DateTimeParameter.values required")
    return out
