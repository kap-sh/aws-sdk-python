"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_s3.errors import DeserializationError, SerializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.analytics_and_operator
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.tag


class _AnalyticsFilter_Prefix(TypedDict):
    Prefix: "aws_sdk_s3.types.prefix.Prefix"


class _AnalyticsFilter_Tag(TypedDict):
    Tag: "aws_sdk_s3.types.tag.Tag"


class _AnalyticsFilter_And(TypedDict):
    And: "aws_sdk_s3.types.analytics_and_operator.AnalyticsAndOperator"


AnalyticsFilter: TypeAlias = (
    _AnalyticsFilter_Prefix | _AnalyticsFilter_Tag | _AnalyticsFilter_And
)


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "Prefix" in value:
        SubElement(el, "Prefix").text = str(value["Prefix"])
    elif "Tag" in value:
        import aws_sdk_s3.types.tag

        aws_sdk_s3.types.tag.serialize_xml(value["Tag"], el, "Tag")
    elif "And" in value:
        import aws_sdk_s3.types.analytics_and_operator

        aws_sdk_s3.types.analytics_and_operator.serialize_xml(value["And"], el, "And")
    else:
        raise SerializationError("AnalyticsFilter: no variant present")


def deserialize_xml(el: Element) -> AnalyticsFilter:
    for child in el:
        if child.tag == "Prefix":
            return {"Prefix": str(child.text or "")}
        elif child.tag == "Tag":
            import aws_sdk_s3.types.tag

            return {"Tag": aws_sdk_s3.types.tag.deserialize_xml(child)}
        elif child.tag == "And":
            import aws_sdk_s3.types.analytics_and_operator

            return {
                "And": aws_sdk_s3.types.analytics_and_operator.deserialize_xml(child)
            }
    raise DeserializationError("AnalyticsFilter: no recognized variant element")
