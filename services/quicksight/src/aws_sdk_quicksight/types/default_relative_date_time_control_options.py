"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultRelativeDateTimeControlOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.commit_mode
    import aws_sdk_quicksight.types.relative_date_time_control_display_options


class DefaultRelativeDateTimeControlOptions(TypedDict):
    display_options: NotRequired[
        "aws_sdk_quicksight.types.relative_date_time_control_display_options.RelativeDateTimeControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    commit_mode: NotRequired["aws_sdk_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configuration of the Apply button on a <code>RelativeDateTimeControl</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultRelativeDateTimeControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import aws_sdk_quicksight.types.relative_date_time_control_display_options

        out["DisplayOptions"] = (
            aws_sdk_quicksight.types.relative_date_time_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "commit_mode" in value:
        import aws_sdk_quicksight.types.commit_mode

        out["CommitMode"] = aws_sdk_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    return out


def deserialize_json(data: dict) -> DefaultRelativeDateTimeControlOptions:
    out: DefaultRelativeDateTimeControlOptions = {}  # type: ignore[typeddict-item]
    if "DisplayOptions" in data:
        import aws_sdk_quicksight.types.relative_date_time_control_display_options

        out["display_options"] = (
            aws_sdk_quicksight.types.relative_date_time_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "CommitMode" in data:
        import aws_sdk_quicksight.types.commit_mode

        out["commit_mode"] = aws_sdk_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    return out
