"""Generated from Smithy shape ``com.amazonaws.sns#MessageAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.message_attribute_value
    import aws_sdk_sns.types.string

MessageAttributeMap: TypeAlias = dict[
    "aws_sdk_sns.types.string.String",
    "aws_sdk_sns.types.message_attribute_value.MessageAttributeValue",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: MessageAttributeMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.message_attribute_value

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.Name", str(key)))
        aws_sdk_sns.types.message_attribute_value.serialize_query(
            value, pairs, f"{prefix}.entry.{n}.Value"
        )


def deserialize_query(el: Element) -> MessageAttributeMap:
    out: MessageAttributeMap = {}
    for entry in el.findall("entry"):
        key_element = entry.find("Name")
        value_element = entry.find("Value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import aws_sdk_sns.types.message_attribute_value

        value = aws_sdk_sns.types.message_attribute_value.deserialize_query(
            value_element
        )
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: MessageAttributeMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.message_attribute_value

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.Name", str(key)))
        aws_sdk_sns.types.message_attribute_value.serialize_query(
            value, pairs, f"{prefix}.{n}.Value"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MessageAttributeMap:
    out: MessageAttributeMap = {}
    for entry in parent.findall(tag):
        key_element = entry.find("Name")
        value_element = entry.find("Value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import aws_sdk_sns.types.message_attribute_value

        value = aws_sdk_sns.types.message_attribute_value.deserialize_query(
            value_element
        )
        out[key] = value
    return out
