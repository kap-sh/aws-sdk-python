"""Generated from Smithy shape ``com.amazonaws.appflow#FieldTypeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.field_type
    import aws_sdk_appflow.types.filter_operator_list
    import aws_sdk_appflow.types.range
    import aws_sdk_appflow.types.string
    import aws_sdk_appflow.types.supported_value_list


class FieldTypeDetails(TypedDict):
    field_type: "aws_sdk_appflow.types.field_type.FieldType"
    """<p> The type of field, such as string, integer, date, and so on. </p>"""
    filter_operators: "aws_sdk_appflow.types.filter_operator_list.FilterOperatorList"
    """<p> The list of operators supported by a field. </p>"""
    supported_values: NotRequired[
        "aws_sdk_appflow.types.supported_value_list.SupportedValueList"
    ]
    r"""<p> The list of values that a field can contain. For example, a Boolean <code>fieldType</code> can have two values: \"true\" and \"false\". </p>"""
    value_regex_pattern: NotRequired["aws_sdk_appflow.types.string.String"]
    """<p>The regular expression pattern for the field name.</p>"""
    supported_date_format: NotRequired["aws_sdk_appflow.types.string.String"]
    """<p>The date format that the field supports.</p>"""
    field_value_range: NotRequired["aws_sdk_appflow.types.range.Range"]
    """<p>The range of values this field can hold.</p>"""
    field_length_range: NotRequired["aws_sdk_appflow.types.range.Range"]
    """<p>This is the allowable length range for this field's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldTypeDetails) -> dict:
    out: dict = {}
    out["fieldType"] = value["field_type"]
    import aws_sdk_appflow.types.filter_operator_list

    out["filterOperators"] = aws_sdk_appflow.types.filter_operator_list.serialize_json(
        value["filter_operators"]
    )
    if "supported_values" in value:
        import aws_sdk_appflow.types.supported_value_list

        out["supportedValues"] = (
            aws_sdk_appflow.types.supported_value_list.serialize_json(
                value["supported_values"]
            )
        )
    if "value_regex_pattern" in value:
        out["valueRegexPattern"] = value["value_regex_pattern"]
    if "supported_date_format" in value:
        out["supportedDateFormat"] = value["supported_date_format"]
    if "field_value_range" in value:
        import aws_sdk_appflow.types.range

        out["fieldValueRange"] = aws_sdk_appflow.types.range.serialize_json(
            value["field_value_range"]
        )
    if "field_length_range" in value:
        import aws_sdk_appflow.types.range

        out["fieldLengthRange"] = aws_sdk_appflow.types.range.serialize_json(
            value["field_length_range"]
        )
    return out


def deserialize_json(data: dict) -> FieldTypeDetails:
    out: FieldTypeDetails = {}  # type: ignore[typeddict-item]
    if "fieldType" in data:
        out["field_type"] = data["fieldType"]
    else:
        raise DeserializationError("FieldTypeDetails.field_type required")
    if "filterOperators" in data:
        import aws_sdk_appflow.types.filter_operator_list

        out["filter_operators"] = (
            aws_sdk_appflow.types.filter_operator_list.deserialize_json(
                data["filterOperators"]
            )
        )
    else:
        raise DeserializationError("FieldTypeDetails.filter_operators required")
    if "supportedValues" in data:
        import aws_sdk_appflow.types.supported_value_list

        out["supported_values"] = (
            aws_sdk_appflow.types.supported_value_list.deserialize_json(
                data["supportedValues"]
            )
        )
    if "valueRegexPattern" in data:
        out["value_regex_pattern"] = data["valueRegexPattern"]
    if "supportedDateFormat" in data:
        out["supported_date_format"] = data["supportedDateFormat"]
    if "fieldValueRange" in data:
        import aws_sdk_appflow.types.range

        out["field_value_range"] = aws_sdk_appflow.types.range.deserialize_json(
            data["fieldValueRange"]
        )
    if "fieldLengthRange" in data:
        import aws_sdk_appflow.types.range

        out["field_length_range"] = aws_sdk_appflow.types.range.deserialize_json(
            data["fieldLengthRange"]
        )
    return out
