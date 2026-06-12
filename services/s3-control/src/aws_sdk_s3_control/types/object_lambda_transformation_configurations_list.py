"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaTransformationConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration

ObjectLambdaTransformationConfigurationsList: TypeAlias = list[
    "aws_sdk_s3_control.types.object_lambda_transformation_configuration.ObjectLambdaTransformationConfiguration"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaTransformationConfigurationsList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_transformation_configuration

        aws_sdk_s3_control.types.object_lambda_transformation_configuration.serialize_xml(
            item, el, "TransformationConfiguration"
        )


def deserialize_xml(el: Element) -> ObjectLambdaTransformationConfigurationsList:
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration

    out: ObjectLambdaTransformationConfigurationsList = []
    for child in el.findall("TransformationConfiguration"):
        out.append(
            aws_sdk_s3_control.types.object_lambda_transformation_configuration.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ObjectLambdaTransformationConfigurationsList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_transformation_configuration

        aws_sdk_s3_control.types.object_lambda_transformation_configuration.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> ObjectLambdaTransformationConfigurationsList:
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration

    out: ObjectLambdaTransformationConfigurationsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.object_lambda_transformation_configuration.deserialize_xml(
                child
            )
        )
    return out
