"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.pivoted_label_list


class PivotConfiguration(TypedDict):
    label_column_name: NotRequired["aws_sdk_quicksight.types.column_name.ColumnName"]
    """<p>The name of the column that contains the labels to be pivoted into separate columns.</p>"""
    pivoted_labels: "aws_sdk_quicksight.types.pivoted_label_list.PivotedLabelList"
    """<p>The list of specific label values to pivot into separate columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotConfiguration) -> dict:
    out: dict = {}
    if "label_column_name" in value:
        out["LabelColumnName"] = value["label_column_name"]
    import aws_sdk_quicksight.types.pivoted_label_list

    out["PivotedLabels"] = aws_sdk_quicksight.types.pivoted_label_list.serialize_json(
        value["pivoted_labels"]
    )
    return out


def deserialize_json(data: dict) -> PivotConfiguration:
    out: PivotConfiguration = {}  # type: ignore[typeddict-item]
    if "LabelColumnName" in data:
        out["label_column_name"] = data["LabelColumnName"]
    if "PivotedLabels" in data:
        import aws_sdk_quicksight.types.pivoted_label_list

        out["pivoted_labels"] = (
            aws_sdk_quicksight.types.pivoted_label_list.deserialize_json(
                data["PivotedLabels"]
            )
        )
    else:
        raise DeserializationError("PivotConfiguration.pivoted_labels required")
    return out
