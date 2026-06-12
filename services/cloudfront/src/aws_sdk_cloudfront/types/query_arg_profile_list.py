"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryArgProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.query_arg_profile

QueryArgProfileList: TypeAlias = list[
    "aws_sdk_cloudfront.types.query_arg_profile.QueryArgProfile"
]


# --- restXml ser/de ---
def serialize_xml(value: QueryArgProfileList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.query_arg_profile

        aws_sdk_cloudfront.types.query_arg_profile.serialize_xml(
            item, el, "QueryArgProfile"
        )


def deserialize_xml(el: Element) -> QueryArgProfileList:
    import aws_sdk_cloudfront.types.query_arg_profile

    out: QueryArgProfileList = []
    for child in el.findall("QueryArgProfile"):
        out.append(aws_sdk_cloudfront.types.query_arg_profile.deserialize_xml(child))
    return out


def serialize_xml_flat(value: QueryArgProfileList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.query_arg_profile

        aws_sdk_cloudfront.types.query_arg_profile.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> QueryArgProfileList:
    import aws_sdk_cloudfront.types.query_arg_profile

    out: QueryArgProfileList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.query_arg_profile.deserialize_xml(child))
    return out
