"""Generated from Smithy shape ``com.amazonaws.ses#ExtensionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.extension_field

ExtensionFieldList: TypeAlias = list["aws_sdk_ses.types.extension_field.ExtensionField"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ExtensionFieldList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.extension_field

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.extension_field.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ExtensionFieldList:
    import aws_sdk_ses.types.extension_field

    out: ExtensionFieldList = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.extension_field.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ExtensionFieldList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.extension_field

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.extension_field.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ExtensionFieldList:
    import aws_sdk_ses.types.extension_field

    out: ExtensionFieldList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.extension_field.deserialize_query(child))
    return out
