"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointForObjectLambdaResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.creation_date
    import aws_sdk_s3_control.types.object_lambda_access_point_alias
    import aws_sdk_s3_control.types.object_lambda_access_point_name
    import aws_sdk_s3_control.types.public_access_block_configuration


class GetAccessPointForObjectLambdaResult(TypedDict):
    name: NotRequired[
        "aws_sdk_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    ]
    """<p>The name of the Object Lambda Access Point.</p>"""
    public_access_block_configuration: NotRequired[
        "aws_sdk_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    """<p>Configuration to block all public access. This setting is turned on and can not be edited. </p>"""
    creation_date: NotRequired["aws_sdk_s3_control.types.creation_date.CreationDate"]
    """<p>The date and time when the specified Object Lambda Access Point was created.</p>"""
    alias: NotRequired[
        "aws_sdk_s3_control.types.object_lambda_access_point_alias.ObjectLambdaAccessPointAlias"
    ]
    """<p>The alias of the Object Lambda Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointForObjectLambdaResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "public_access_block_configuration" in value:
        import aws_sdk_s3_control.types.public_access_block_configuration

        aws_sdk_s3_control.types.public_access_block_configuration.serialize_xml(
            value["public_access_block_configuration"],
            el,
            "PublicAccessBlockConfiguration",
        )
    if "creation_date" in value:
        import aws_sdk_s3_control.types.creation_date

        aws_sdk_s3_control.types.creation_date.serialize_xml(
            value["creation_date"], el, "CreationDate"
        )
    if "alias" in value:
        import aws_sdk_s3_control.types.object_lambda_access_point_alias

        aws_sdk_s3_control.types.object_lambda_access_point_alias.serialize_xml(
            value["alias"], el, "Alias"
        )


def deserialize_xml(el: Element) -> GetAccessPointForObjectLambdaResult:
    out: GetAccessPointForObjectLambdaResult = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import aws_sdk_s3_control.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            aws_sdk_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import aws_sdk_s3_control.types.creation_date

        out["creation_date"] = aws_sdk_s3_control.types.creation_date.deserialize_xml(
            child_creation_date
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
