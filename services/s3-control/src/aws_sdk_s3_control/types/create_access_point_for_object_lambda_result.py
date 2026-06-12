"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessPointForObjectLambdaResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_access_point_alias
    import aws_sdk_s3_control.types.object_lambda_access_point_arn


class CreateAccessPointForObjectLambdaResult(TypedDict):
    object_lambda_access_point_arn: NotRequired[
        "aws_sdk_s3_control.types.object_lambda_access_point_arn.ObjectLambdaAccessPointArn"
    ]
    """<p>Specifies the ARN for the Object Lambda Access Point.</p>"""
    alias: NotRequired[
        "aws_sdk_s3_control.types.object_lambda_access_point_alias.ObjectLambdaAccessPointAlias"
    ]
    """<p>The alias of the Object Lambda Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateAccessPointForObjectLambdaResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "object_lambda_access_point_arn" in value:
        SubElement(el, "ObjectLambdaAccessPointArn").text = str(
            value["object_lambda_access_point_arn"]
        )
    if "alias" in value:
        import aws_sdk_s3_control.types.object_lambda_access_point_alias

        aws_sdk_s3_control.types.object_lambda_access_point_alias.serialize_xml(
            value["alias"], el, "Alias"
        )


def deserialize_xml(el: Element) -> CreateAccessPointForObjectLambdaResult:
    out: CreateAccessPointForObjectLambdaResult = {}  # type: ignore[typeddict-item]
    child_object_lambda_access_point_arn = el.find("ObjectLambdaAccessPointArn")
    if child_object_lambda_access_point_arn is not None:
        out["object_lambda_access_point_arn"] = str(
            child_object_lambda_access_point_arn.text or ""
        )
    child_alias = el.find("Alias")
    if child_alias is not None:
        import aws_sdk_s3_control.types.object_lambda_access_point_alias

        out["alias"] = (
            aws_sdk_s3_control.types.object_lambda_access_point_alias.deserialize_xml(
                child_alias
            )
        )
    return out
