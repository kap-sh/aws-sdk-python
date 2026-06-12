"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessGrantsInstanceForPrefixResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_grants_instance_arn
    import aws_sdk_s3_control.types.access_grants_instance_id


class GetAccessGrantsInstanceForPrefixResult(TypedDict):
    access_grants_instance_arn: NotRequired[
        "aws_sdk_s3_control.types.access_grants_instance_arn.AccessGrantsInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 Access Grants instance. </p>"""
    access_grants_instance_id: NotRequired[
        "aws_sdk_s3_control.types.access_grants_instance_id.AccessGrantsInstanceId"
    ]
    """<p>The ID of the S3 Access Grants instance. The ID is <code>default</code>. You can have one S3 Access Grants instance per Region per account. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessGrantsInstanceForPrefixResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "access_grants_instance_arn" in value:
        SubElement(el, "AccessGrantsInstanceArn").text = str(
            value["access_grants_instance_arn"]
        )
    if "access_grants_instance_id" in value:
        SubElement(el, "AccessGrantsInstanceId").text = str(
            value["access_grants_instance_id"]
        )


def deserialize_xml(el: Element) -> GetAccessGrantsInstanceForPrefixResult:
    out: GetAccessGrantsInstanceForPrefixResult = {}  # type: ignore[typeddict-item]
    child_access_grants_instance_arn = el.find("AccessGrantsInstanceArn")
    if child_access_grants_instance_arn is not None:
        out["access_grants_instance_arn"] = str(
            child_access_grants_instance_arn.text or ""
        )
    child_access_grants_instance_id = el.find("AccessGrantsInstanceId")
    if child_access_grants_instance_id is not None:
        out["access_grants_instance_id"] = str(
            child_access_grants_instance_id.text or ""
        )
    return out
