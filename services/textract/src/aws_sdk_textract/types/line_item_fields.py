"""Generated from Smithy shape ``com.amazonaws.textract#LineItemFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.expense_field_list


class LineItemFields(TypedDict, closed=True):
    line_item_expense_fields: NotRequired[
        "aws_sdk_textract.types.expense_field_list.ExpenseFieldList"
    ]
    """<p>ExpenseFields used to show information from detected lines on a table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineItemFields) -> dict:
    out: dict = {}
    if "line_item_expense_fields" in value:
        import aws_sdk_textract.types.expense_field_list

        out["LineItemExpenseFields"] = (
            aws_sdk_textract.types.expense_field_list.serialize_aws_json_1_1(
                value["line_item_expense_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineItemFields:
    out: LineItemFields = {}  # type: ignore[typeddict-item]
    if "LineItemExpenseFields" in data:
        import aws_sdk_textract.types.expense_field_list

        out["line_item_expense_fields"] = (
            aws_sdk_textract.types.expense_field_list.deserialize_aws_json_1_1(
                data["LineItemExpenseFields"]
            )
        )
    return out
