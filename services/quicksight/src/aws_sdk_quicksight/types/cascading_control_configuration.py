"""Generated from Smithy shape ``com.amazonaws.quicksight#CascadingControlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cascading_control_source_list


class CascadingControlConfiguration(TypedDict, closed=True):
    source_controls: NotRequired[
        "aws_sdk_quicksight.types.cascading_control_source_list.CascadingControlSourceList"
    ]
    """<p>A list of source controls that determine the values that are used in the current control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CascadingControlConfiguration) -> dict:
    out: dict = {}
    if "source_controls" in value:
        import aws_sdk_quicksight.types.cascading_control_source_list

        out["SourceControls"] = (
            aws_sdk_quicksight.types.cascading_control_source_list.serialize_json(
                value["source_controls"]
            )
        )
    return out


def deserialize_json(data: dict) -> CascadingControlConfiguration:
    out: CascadingControlConfiguration = {}  # type: ignore[typeddict-item]
    if "SourceControls" in data:
        import aws_sdk_quicksight.types.cascading_control_source_list

        out["source_controls"] = (
            aws_sdk_quicksight.types.cascading_control_source_list.deserialize_json(
                data["SourceControls"]
            )
        )
    return out
