"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaTransformationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_content_transformation
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration_actions_list


class ObjectLambdaTransformationConfiguration(TypedDict):
    actions: "aws_sdk_s3_control.types.object_lambda_transformation_configuration_actions_list.ObjectLambdaTransformationConfigurationActionsList"
    """<p>A container for the action of an Object Lambda Access Point configuration. Valid inputs are <code>GetObject</code>, <code>ListObjects</code>, <code>HeadObject</code>, and <code>ListObjectsV2</code>.</p>"""
    content_transformation: "aws_sdk_s3_control.types.object_lambda_content_transformation.ObjectLambdaContentTransformation"
    """<p>A container for the content transformation of an Object Lambda Access Point configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaTransformationConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.object_lambda_transformation_configuration_actions_list

    aws_sdk_s3_control.types.object_lambda_transformation_configuration_actions_list.serialize_xml(
        value["actions"], el, "Actions"
    )
    import aws_sdk_s3_control.types.object_lambda_content_transformation

    aws_sdk_s3_control.types.object_lambda_content_transformation.serialize_xml(
        value["content_transformation"], el, "ContentTransformation"
    )


def deserialize_xml(el: Element) -> ObjectLambdaTransformationConfiguration:
    out: ObjectLambdaTransformationConfiguration = {}  # type: ignore[typeddict-item]
    child_actions = el.find("Actions")
    if child_actions is not None:
        import aws_sdk_s3_control.types.object_lambda_transformation_configuration_actions_list

        out["actions"] = (
            aws_sdk_s3_control.types.object_lambda_transformation_configuration_actions_list.deserialize_xml(
                child_actions
            )
        )
    else:
        raise DeserializationError(
            "ObjectLambdaTransformationConfiguration.actions required"
        )
    child_content_transformation = el.find("ContentTransformation")
    if child_content_transformation is not None:
        import aws_sdk_s3_control.types.object_lambda_content_transformation

        out["content_transformation"] = (
            aws_sdk_s3_control.types.object_lambda_content_transformation.deserialize_xml(
                child_content_transformation
            )
        )
    else:
        raise DeserializationError(
            "ObjectLambdaTransformationConfiguration.content_transformation required"
        )
    return out
