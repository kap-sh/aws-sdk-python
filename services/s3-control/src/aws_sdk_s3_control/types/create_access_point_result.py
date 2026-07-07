"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessPointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.alias
    import aws_sdk_s3_control.types.s3_access_point_arn


class CreateAccessPointResult(TypedDict, closed=True):
    access_point_arn: NotRequired[
        "aws_sdk_s3_control.types.s3_access_point_arn.S3AccessPointArn"
    ]
    """<p>The ARN of the access point.</p> <note> <p>This is only supported by Amazon S3 on Outposts.</p> </note>"""
    alias: NotRequired["aws_sdk_s3_control.types.alias.Alias"]
    """<p>The name or alias of the access point.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAccessPointResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "access_point_arn" in value:
        SubElement(el, "AccessPointArn").text = str(value["access_point_arn"])
    if "alias" in value:
        SubElement(el, "Alias").text = str(value["alias"])


def deserialize_xml(el: Element) -> CreateAccessPointResult:
    out: CreateAccessPointResult = {}  # type: ignore[typeddict-item]
    child_access_point_arn = el.find("AccessPointArn")
    if child_access_point_arn is not None:
        out["access_point_arn"] = str(child_access_point_arn.text or "")
    child_alias = el.find("Alias")
    if child_alias is not None:
        out["alias"] = str(child_alias.text or "")
    return out
