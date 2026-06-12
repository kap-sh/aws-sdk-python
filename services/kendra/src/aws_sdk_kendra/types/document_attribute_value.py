"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_string_list_value
    import aws_sdk_kendra.types.document_attribute_string_value
    import aws_sdk_kendra.types.long
    import aws_sdk_kendra.types.timestamp


class DocumentAttributeValue(TypedDict):
    string_value: NotRequired[
        "aws_sdk_kendra.types.document_attribute_string_value.DocumentAttributeStringValue"
    ]
    """<p>A string, such as \"department\".</p>"""
    string_list_value: NotRequired[
        "aws_sdk_kendra.types.document_attribute_string_list_value.DocumentAttributeStringListValue"
    ]
    """<p>A list of strings. The default maximum length or number of strings is 10.</p>"""
    long_value: NotRequired["aws_sdk_kendra.types.long.Long"]
    """<p>A long integer value.</p>"""
    date_value: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>A date expressed as an ISO 8601 string.</p> <p>It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeValue) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    if "string_list_value" in value:
        import aws_sdk_kendra.types.document_attribute_string_list_value

        out["StringListValue"] = (
            aws_sdk_kendra.types.document_attribute_string_list_value.serialize_aws_json_1_1(
                value["string_list_value"]
            )
        )
    if "long_value" in value:
        out["LongValue"] = value["long_value"]
    if "date_value" in value:
        import aws_sdk_kendra.types.timestamp

        out["DateValue"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["date_value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttributeValue:
    out: DocumentAttributeValue = {}  # type: ignore[typeddict-item]
    if "StringValue" in data:
        out["string_value"] = data["StringValue"]
    if "StringListValue" in data:
        import aws_sdk_kendra.types.document_attribute_string_list_value

        out["string_list_value"] = (
            aws_sdk_kendra.types.document_attribute_string_list_value.deserialize_aws_json_1_1(
                data["StringListValue"]
            )
        )
    if "LongValue" in data:
        out["long_value"] = data["LongValue"]
    if "DateValue" in data:
        import aws_sdk_kendra.types.timestamp

        out["date_value"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["DateValue"]
        )
    return out
