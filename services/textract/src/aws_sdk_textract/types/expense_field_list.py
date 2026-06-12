"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.expense_field

ExpenseFieldList: TypeAlias = list["aws_sdk_textract.types.expense_field.ExpenseField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseFieldList) -> list:
    import aws_sdk_textract.types.expense_field

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.expense_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExpenseFieldList:
    import aws_sdk_textract.types.expense_field

    out: ExpenseFieldList = []
    for item in data:
        out.append(aws_sdk_textract.types.expense_field.deserialize_aws_json_1_1(item))
    return out
