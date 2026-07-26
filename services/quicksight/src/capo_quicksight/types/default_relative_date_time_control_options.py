"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultRelativeDateTimeControlOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.commit_mode
    import capo_quicksight.types.relative_date_time_control_display_options


class DefaultRelativeDateTimeControlOptions(TypedDict, closed=True):
    display_options: NotRequired[
        "capo_quicksight.types.relative_date_time_control_display_options.RelativeDateTimeControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    commit_mode: NotRequired["capo_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configuration of the Apply button on a <code>RelativeDateTimeControl</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultRelativeDateTimeControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import capo_quicksight.types.relative_date_time_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.relative_date_time_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "commit_mode" in value:
        import capo_quicksight.types.commit_mode

        out["CommitMode"] = capo_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    return out


def deserialize_json(data: dict) -> DefaultRelativeDateTimeControlOptions:
    out: DefaultRelativeDateTimeControlOptions = {}  # type: ignore[typeddict-item]
    if "DisplayOptions" in data:
        import capo_quicksight.types.relative_date_time_control_display_options

        out["display_options"] = (
            capo_quicksight.types.relative_date_time_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if "CommitMode" in data:
        import capo_quicksight.types.commit_mode

        out["commit_mode"] = capo_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    return out
