"""Generated from Smithy shape ``com.amazonaws.s3control#S3SetObjectAclOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_access_control_policy


class S3SetObjectAclOperation(TypedDict):
    access_control_policy: NotRequired[
        "aws_sdk_s3_control.types.s3_access_control_policy.S3AccessControlPolicy"
    ]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3SetObjectAclOperation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "access_control_policy" in value:
        import aws_sdk_s3_control.types.s3_access_control_policy

        aws_sdk_s3_control.types.s3_access_control_policy.serialize_xml(
            value["access_control_policy"], el, "AccessControlPolicy"
        )


def deserialize_xml(el: Element) -> S3SetObjectAclOperation:
    out: S3SetObjectAclOperation = {}  # type: ignore[typeddict-item]
    child_access_control_policy = el.find("AccessControlPolicy")
    if child_access_control_policy is not None:
        import aws_sdk_s3_control.types.s3_access_control_policy

        out["access_control_policy"] = (
            aws_sdk_s3_control.types.s3_access_control_policy.deserialize_xml(
                child_access_control_policy
            )
        )
    return out
