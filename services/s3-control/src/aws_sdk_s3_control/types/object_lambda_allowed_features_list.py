"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaAllowedFeaturesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_allowed_feature

ObjectLambdaAllowedFeaturesList: TypeAlias = list[
    "aws_sdk_s3_control.types.object_lambda_allowed_feature.ObjectLambdaAllowedFeature"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaAllowedFeaturesList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_allowed_feature

        aws_sdk_s3_control.types.object_lambda_allowed_feature.serialize_xml(
            item, el, "AllowedFeature"
        )


def deserialize_xml(el: Element) -> ObjectLambdaAllowedFeaturesList:
    import aws_sdk_s3_control.types.object_lambda_allowed_feature

    out: ObjectLambdaAllowedFeaturesList = []
    for child in el.findall("AllowedFeature"):
        out.append(
            aws_sdk_s3_control.types.object_lambda_allowed_feature.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ObjectLambdaAllowedFeaturesList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.object_lambda_allowed_feature

        aws_sdk_s3_control.types.object_lambda_allowed_feature.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectLambdaAllowedFeaturesList:
    import aws_sdk_s3_control.types.object_lambda_allowed_feature

    out: ObjectLambdaAllowedFeaturesList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.object_lambda_allowed_feature.deserialize_xml(
                child
            )
        )
    return out
