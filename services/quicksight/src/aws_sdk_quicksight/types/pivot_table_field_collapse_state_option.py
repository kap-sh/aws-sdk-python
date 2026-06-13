"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseStateOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_field_collapse_state
    import aws_sdk_quicksight.types.pivot_table_field_collapse_state_target


class PivotTableFieldCollapseStateOption(TypedDict):
    target: "aws_sdk_quicksight.types.pivot_table_field_collapse_state_target.PivotTableFieldCollapseStateTarget"
    """<p>A tagged-union object that sets the collapse state.</p>"""
    state: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_field_collapse_state.PivotTableFieldCollapseState"
    ]
    """<p>The state of the field target of a pivot table. Choose one of the following options:</p> <ul> <li> <p> <code>COLLAPSED</code> </p> </li> <li> <p> <code>EXPANDED</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldCollapseStateOption) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.pivot_table_field_collapse_state_target

    out["Target"] = (
        aws_sdk_quicksight.types.pivot_table_field_collapse_state_target.serialize_json(
            value["target"]
        )
    )
    if "state" in value:
        import aws_sdk_quicksight.types.pivot_table_field_collapse_state

        out["State"] = (
            aws_sdk_quicksight.types.pivot_table_field_collapse_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldCollapseStateOption:
    out: PivotTableFieldCollapseStateOption = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        import aws_sdk_quicksight.types.pivot_table_field_collapse_state_target

        out["target"] = (
            aws_sdk_quicksight.types.pivot_table_field_collapse_state_target.deserialize_json(
                data["Target"]
            )
        )
    else:
        raise DeserializationError("PivotTableFieldCollapseStateOption.target required")
    if "State" in data:
        import aws_sdk_quicksight.types.pivot_table_field_collapse_state

        out["state"] = (
            aws_sdk_quicksight.types.pivot_table_field_collapse_state.deserialize_json(
                data["State"]
            )
        )
    return out
