"""Generated from Smithy shape ``com.amazonaws.sns#MessageAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.binary
    import aws_sdk_sns.types.string


class MessageAttributeValue(TypedDict, closed=True):
    data_type: "aws_sdk_sns.types.string.String"
    r"""<p>Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see <a href=\"https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes\">Message Attribute Data Types</a>.</p>"""
    string_value: NotRequired["aws_sdk_sns.types.string.String"]
    r"""<p>Strings are Unicode with UTF8 binary encoding. For a list of code values, see <a href=\"https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters\">ASCII Printable Characters</a>.</p>"""
    binary_value: NotRequired["aws_sdk_sns.types.binary.Binary"]
    """<p>Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageAttributeValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DataType", str(value["data_type"])))
    if "string_value" in value:
        pairs.append((f"{prefix}.StringValue", str(value["string_value"])))
    if "binary_value" in value:
        import aws_sdk_sns.types.binary

        aws_sdk_sns.types.binary.serialize_query(
            value["binary_value"], pairs, f"{prefix}.BinaryValue"
        )


def deserialize_query(el: Element) -> MessageAttributeValue:
    out: MessageAttributeValue = {}  # type: ignore[typeddict-item]
    child_data_type = el.find("DataType")
    if child_data_type is not None:
        out["data_type"] = str(child_data_type.text or "")
    else:
        raise DeserializationError("MessageAttributeValue.data_type required")
    child_string_value = el.find("StringValue")
    if child_string_value is not None:
        out["string_value"] = str(child_string_value.text or "")
    child_binary_value = el.find("BinaryValue")
    if child_binary_value is not None:
        import aws_sdk_sns.types.binary

        out["binary_value"] = aws_sdk_sns.types.binary.deserialize_query(
            child_binary_value
        )
    return out
