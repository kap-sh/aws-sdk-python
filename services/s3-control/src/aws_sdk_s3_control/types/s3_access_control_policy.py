"""Generated from Smithy shape ``com.amazonaws.s3control#S3AccessControlPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_access_control_list
    import aws_sdk_s3_control.types.s3_canned_access_control_list


class S3AccessControlPolicy(TypedDict):
    access_control_list: NotRequired[
        "aws_sdk_s3_control.types.s3_access_control_list.S3AccessControlList"
    ]
    """<p></p>"""
    canned_access_control_list: NotRequired[
        "aws_sdk_s3_control.types.s3_canned_access_control_list.S3CannedAccessControlList"
    ]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3AccessControlPolicy, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "access_control_list" in value:
        import aws_sdk_s3_control.types.s3_access_control_list

        aws_sdk_s3_control.types.s3_access_control_list.serialize_xml(
            value["access_control_list"], el, "AccessControlList"
        )
    if "canned_access_control_list" in value:
        import aws_sdk_s3_control.types.s3_canned_access_control_list

        aws_sdk_s3_control.types.s3_canned_access_control_list.serialize_xml(
            value["canned_access_control_list"], el, "CannedAccessControlList"
        )


def deserialize_xml(el: Element) -> S3AccessControlPolicy:
    out: S3AccessControlPolicy = {}  # type: ignore[typeddict-item]
    child_access_control_list = el.find("AccessControlList")
    if child_access_control_list is not None:
        import aws_sdk_s3_control.types.s3_access_control_list

        out["access_control_list"] = (
            aws_sdk_s3_control.types.s3_access_control_list.deserialize_xml(
                child_access_control_list
            )
        )
    child_canned_access_control_list = el.find("CannedAccessControlList")
    if child_canned_access_control_list is not None:
        import aws_sdk_s3_control.types.s3_canned_access_control_list

        out["canned_access_control_list"] = (
            aws_sdk_s3_control.types.s3_canned_access_control_list.deserialize_xml(
                child_canned_access_control_list
            )
        )
    return out
