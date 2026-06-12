"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaAccessPointList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_access_point

ObjectLambdaAccessPointList: TypeAlias = list[
    "aws_sdk_s3_control.types.object_lambda_access_point.ObjectLambdaAccessPoint"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaAccessPointList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_access_point

        aws_sdk_s3_control.types.object_lambda_access_point.serialize_xml(
            item, el, "ObjectLambdaAccessPoint"
        )


def deserialize_xml(el: Element) -> ObjectLambdaAccessPointList:
    import aws_sdk_s3_control.types.object_lambda_access_point

    out: ObjectLambdaAccessPointList = []
    for child in el.findall("ObjectLambdaAccessPoint"):
        out.append(
            aws_sdk_s3_control.types.object_lambda_access_point.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ObjectLambdaAccessPointList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_access_point

        aws_sdk_s3_control.types.object_lambda_access_point.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectLambdaAccessPointList:
    import aws_sdk_s3_control.types.object_lambda_access_point

    out: ObjectLambdaAccessPointList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.object_lambda_access_point.deserialize_xml(child)
        )
    return out
