"""Generated from Smithy shape ``com.amazonaws.s3#MetricsFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_s3.errors import DeserializationError, SerializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.metrics_and_operator
    import aws_sdk_s3.types.access_point_arn
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.tag


class _MetricsFilter_Prefix(TypedDict):
    Prefix: "aws_sdk_s3.types.prefix.Prefix"


class _MetricsFilter_Tag(TypedDict):
    Tag: "aws_sdk_s3.types.tag.Tag"


class _MetricsFilter_AccessPointArn(TypedDict):
    AccessPointArn: "aws_sdk_s3.types.access_point_arn.AccessPointArn"


class _MetricsFilter_And(TypedDict):
    And: "aws_sdk_s3.types.metrics_and_operator.MetricsAndOperator"


MetricsFilter: TypeAlias = (
    _MetricsFilter_Prefix
    | _MetricsFilter_Tag
    | _MetricsFilter_AccessPointArn
    | _MetricsFilter_And
)


# --- restXml ser/de ---
def serialize_xml(value: MetricsFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "Prefix" in value:
        SubElement(el, "Prefix").text = str(value["Prefix"])
    elif "Tag" in value:
        import aws_sdk_s3.types.tag

        aws_sdk_s3.types.tag.serialize_xml(value["Tag"], el, "Tag")
    elif "AccessPointArn" in value:
        SubElement(el, "AccessPointArn").text = str(value["AccessPointArn"])
    elif "And" in value:
        import aws_sdk_s3.types.metrics_and_operator

        aws_sdk_s3.types.metrics_and_operator.serialize_xml(value["And"], el, "And")
    else:
        raise SerializationError("MetricsFilter: no variant present")


def deserialize_xml(el: Element) -> MetricsFilter:
    for child in el:
        if child.tag == "Prefix":
            return {"Prefix": str(child.text or "")}
        elif child.tag == "Tag":
            import aws_sdk_s3.types.tag

            return {"Tag": aws_sdk_s3.types.tag.deserialize_xml(child)}
        elif child.tag == "AccessPointArn":
            return {"AccessPointArn": str(child.text or "")}
        elif child.tag == "And":
            import aws_sdk_s3.types.metrics_and_operator

            return {"And": aws_sdk_s3.types.metrics_and_operator.deserialize_xml(child)}
    raise DeserializationError("MetricsFilter: no recognized variant element")
