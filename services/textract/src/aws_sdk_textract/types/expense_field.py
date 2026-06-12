"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.expense_currency
    import aws_sdk_textract.types.expense_detection
    import aws_sdk_textract.types.expense_group_property_list
    import aws_sdk_textract.types.expense_type
    import aws_sdk_textract.types.u_integer


class ExpenseField(TypedDict):
    type: NotRequired["aws_sdk_textract.types.expense_type.ExpenseType"]
    """<p>The implied label of a detected element. Present alongside LabelDetection for explicit elements.</p>"""
    label_detection: NotRequired[
        "aws_sdk_textract.types.expense_detection.ExpenseDetection"
    ]
    """<p>The explicitly stated label of a detected element.</p>"""
    value_detection: NotRequired[
        "aws_sdk_textract.types.expense_detection.ExpenseDetection"
    ]
    """<p>The value of a detected element. Present in explicit and implicit elements.</p>"""
    page_number: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>The page number the value was detected on.</p>"""
    currency: NotRequired["aws_sdk_textract.types.expense_currency.ExpenseCurrency"]
    """<p>Shows the kind of currency, both the code and confidence associated with any monatary value detected.</p>"""
    group_properties: NotRequired[
        "aws_sdk_textract.types.expense_group_property_list.ExpenseGroupPropertyList"
    ]
    """<p>Shows which group a response object belongs to, such as whether an address line belongs to the vendor's address or the recipent's address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseField) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_textract.types.expense_type

        out["Type"] = aws_sdk_textract.types.expense_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "label_detection" in value:
        import aws_sdk_textract.types.expense_detection

        out["LabelDetection"] = (
            aws_sdk_textract.types.expense_detection.serialize_aws_json_1_1(
                value["label_detection"]
            )
        )
    if "value_detection" in value:
        import aws_sdk_textract.types.expense_detection

        out["ValueDetection"] = (
            aws_sdk_textract.types.expense_detection.serialize_aws_json_1_1(
                value["value_detection"]
            )
        )
    if "page_number" in value:
        out["PageNumber"] = value["page_number"]
    if "currency" in value:
        import aws_sdk_textract.types.expense_currency

        out["Currency"] = (
            aws_sdk_textract.types.expense_currency.serialize_aws_json_1_1(
                value["currency"]
            )
        )
    if "group_properties" in value:
        import aws_sdk_textract.types.expense_group_property_list

        out["GroupProperties"] = (
            aws_sdk_textract.types.expense_group_property_list.serialize_aws_json_1_1(
                value["group_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseField:
    out: ExpenseField = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_textract.types.expense_type

        out["type"] = aws_sdk_textract.types.expense_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "LabelDetection" in data:
        import aws_sdk_textract.types.expense_detection

        out["label_detection"] = (
            aws_sdk_textract.types.expense_detection.deserialize_aws_json_1_1(
                data["LabelDetection"]
            )
        )
    if "ValueDetection" in data:
        import aws_sdk_textract.types.expense_detection

        out["value_detection"] = (
            aws_sdk_textract.types.expense_detection.deserialize_aws_json_1_1(
                data["ValueDetection"]
            )
        )
    if "PageNumber" in data:
        out["page_number"] = data["PageNumber"]
    if "Currency" in data:
        import aws_sdk_textract.types.expense_currency

        out["currency"] = (
            aws_sdk_textract.types.expense_currency.deserialize_aws_json_1_1(
                data["Currency"]
            )
        )
    if "GroupProperties" in data:
        import aws_sdk_textract.types.expense_group_property_list

        out["group_properties"] = (
            aws_sdk_textract.types.expense_group_property_list.deserialize_aws_json_1_1(
                data["GroupProperties"]
            )
        )
    return out
