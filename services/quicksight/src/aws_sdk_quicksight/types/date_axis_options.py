"""Generated from Smithy shape ``com.amazonaws.quicksight#DateAxisOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visibility


class DateAxisOptions(TypedDict):
    missing_date_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines whether or not missing dates are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateAxisOptions) -> dict:
    out: dict = {}
    if "missing_date_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["MissingDateVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["missing_date_visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateAxisOptions:
    out: DateAxisOptions = {}  # type: ignore[typeddict-item]
    if "MissingDateVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["missing_date_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["MissingDateVisibility"]
            )
        )
    return out
