"""Generated from Smithy shape ``com.amazonaws.quicksight#LogicalTableSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.join_instruction
    import aws_sdk_quicksight.types.physical_table_id


class LogicalTableSource(TypedDict):
    join_instruction: NotRequired[
        "aws_sdk_quicksight.types.join_instruction.JoinInstruction"
    ]
    """<p>Specifies the result of a join of two logical tables.</p>"""
    physical_table_id: NotRequired[
        "aws_sdk_quicksight.types.physical_table_id.PhysicalTableId"
    ]
    """<p>Physical table ID.</p>"""
    data_set_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Number (ARN) of the parent dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogicalTableSource) -> dict:
    out: dict = {}
    if "join_instruction" in value:
        import aws_sdk_quicksight.types.join_instruction

        out["JoinInstruction"] = (
            aws_sdk_quicksight.types.join_instruction.serialize_json(
                value["join_instruction"]
            )
        )
    if "physical_table_id" in value:
        out["PhysicalTableId"] = value["physical_table_id"]
    if "data_set_arn" in value:
        out["DataSetArn"] = value["data_set_arn"]
    return out


def deserialize_json(data: dict) -> LogicalTableSource:
    out: LogicalTableSource = {}  # type: ignore[typeddict-item]
    if "JoinInstruction" in data:
        import aws_sdk_quicksight.types.join_instruction

        out["join_instruction"] = (
            aws_sdk_quicksight.types.join_instruction.deserialize_json(
                data["JoinInstruction"]
            )
        )
    if "PhysicalTableId" in data:
        out["physical_table_id"] = data["PhysicalTableId"]
    if "DataSetArn" in data:
        out["data_set_arn"] = data["DataSetArn"]
    return out
