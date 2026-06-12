"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaTransformationConfigurationActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration_action

ObjectLambdaTransformationConfigurationActionsList: TypeAlias = list[
    "aws_sdk_s3_control.types.object_lambda_transformation_configuration_action.ObjectLambdaTransformationConfigurationAction"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaTransformationConfigurationActionsList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_transformation_configuration_action

        aws_sdk_s3_control.types.object_lambda_transformation_configuration_action.serialize_xml(
            item, el, "Action"
        )


def deserialize_xml(el: Element) -> ObjectLambdaTransformationConfigurationActionsList:
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration_action

    out: ObjectLambdaTransformationConfigurationActionsList = []
    for child in el.findall("Action"):
        out.append(
            aws_sdk_s3_control.types.object_lambda_transformation_configuration_action.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ObjectLambdaTransformationConfigurationActionsList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_transformation_configuration_action

        aws_sdk_s3_control.types.object_lambda_transformation_configuration_action.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> ObjectLambdaTransformationConfigurationActionsList:
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration_action

    out: ObjectLambdaTransformationConfigurationActionsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.object_lambda_transformation_configuration_action.deserialize_xml(
                child
            )
        )
    return out
