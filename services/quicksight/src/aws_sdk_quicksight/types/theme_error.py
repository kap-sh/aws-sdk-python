"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.theme_error_type


class ThemeError(TypedDict, closed=True):
    type: NotRequired["aws_sdk_quicksight.types.theme_error_type.ThemeErrorType"]
    """<p>The type of error.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeError) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_quicksight.types.theme_error_type

        out["Type"] = aws_sdk_quicksight.types.theme_error_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThemeError:
    out: ThemeError = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_quicksight.types.theme_error_type

        out["type"] = aws_sdk_quicksight.types.theme_error_type.deserialize_json(
            data["Type"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
