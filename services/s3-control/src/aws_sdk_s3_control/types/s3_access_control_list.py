"""Generated from Smithy shape ``com.amazonaws.s3control#S3AccessControlList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_grant_list
    import aws_sdk_s3_control.types.s3_object_owner


class S3AccessControlList(TypedDict, closed=True):
    owner: "aws_sdk_s3_control.types.s3_object_owner.S3ObjectOwner"
    """<p></p>"""
    grants: NotRequired["aws_sdk_s3_control.types.s3_grant_list.S3GrantList"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3AccessControlList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.s3_object_owner

    aws_sdk_s3_control.types.s3_object_owner.serialize_xml(value["owner"], el, "Owner")
    if "grants" in value:
        import aws_sdk_s3_control.types.s3_grant_list

        aws_sdk_s3_control.types.s3_grant_list.serialize_xml(
            value["grants"], el, "Grants"
        )


def deserialize_xml(el: Element) -> S3AccessControlList:
    out: S3AccessControlList = {}  # type: ignore[typeddict-item]
    child_owner = el.find("Owner")
    if child_owner is not None:
        import aws_sdk_s3_control.types.s3_object_owner

        out["owner"] = aws_sdk_s3_control.types.s3_object_owner.deserialize_xml(
            child_owner
        )
    else:
        raise DeserializationError("S3AccessControlList.owner required")
    child_grants = el.find("Grants")
    if child_grants is not None:
        import aws_sdk_s3_control.types.s3_grant_list

        out["grants"] = aws_sdk_s3_control.types.s3_grant_list.deserialize_xml(
            child_grants
        )
    return out
