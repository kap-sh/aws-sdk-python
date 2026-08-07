"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaAccessPointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_lambda_access_point

ObjectLambdaAccessPointList: TypeAlias = list[
    "capo_s3_control.types.object_lambda_access_point.ObjectLambdaAccessPoint"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaAccessPointList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.object_lambda_access_point

        capo_s3_control.types.object_lambda_access_point.serialize_xml(
            item, el, "ObjectLambdaAccessPoint"
        )


def deserialize_xml(el: Element) -> ObjectLambdaAccessPointList:
    import capo_s3_control.types.object_lambda_access_point

    out: ObjectLambdaAccessPointList = []
    for child in el.findall("ObjectLambdaAccessPoint"):
        out.append(
            capo_s3_control.types.object_lambda_access_point.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ObjectLambdaAccessPointList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.object_lambda_access_point

        capo_s3_control.types.object_lambda_access_point.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectLambdaAccessPointList:
    import capo_s3_control.types.object_lambda_access_point

    out: ObjectLambdaAccessPointList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.object_lambda_access_point.deserialize_xml(child)
        )
    return out
