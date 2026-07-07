"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaContentTransformation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.aws_lambda_transformation


class _ObjectLambdaContentTransformation_AwsLambda(TypedDict, closed=True):
    AwsLambda: (
        "aws_sdk_s3_control.types.aws_lambda_transformation.AwsLambdaTransformation"
    )


ObjectLambdaContentTransformation: TypeAlias = (
    _ObjectLambdaContentTransformation_AwsLambda
)


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaContentTransformation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "AwsLambda" in value:
        import aws_sdk_s3_control.types.aws_lambda_transformation

        aws_sdk_s3_control.types.aws_lambda_transformation.serialize_xml(
            value["AwsLambda"], el, "AwsLambda"
        )
    else:
        raise SerializationError(
            "ObjectLambdaContentTransformation: no variant present"
        )


def deserialize_xml(el: Element) -> ObjectLambdaContentTransformation:
    for child in el:
        if child.tag == "AwsLambda":
            import aws_sdk_s3_control.types.aws_lambda_transformation

            return {
                "AwsLambda": aws_sdk_s3_control.types.aws_lambda_transformation.deserialize_xml(
                    child
                )
            }
    raise DeserializationError(
        "ObjectLambdaContentTransformation: no recognized variant element"
    )
