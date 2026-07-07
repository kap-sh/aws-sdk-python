"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectLockConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_lock_configuration


class GetObjectLockConfigurationOutput(TypedDict, closed=True):
    object_lock_configuration: NotRequired[
        "aws_sdk_s3.types.object_lock_configuration.ObjectLockConfiguration"
    ]
    """<p>The specified bucket's Object Lock configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetObjectLockConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "object_lock_configuration" in value:
        import aws_sdk_s3.types.object_lock_configuration

        aws_sdk_s3.types.object_lock_configuration.serialize_xml(
            value["object_lock_configuration"], el, "ObjectLockConfiguration"
        )


def deserialize_xml(el: Element) -> GetObjectLockConfigurationOutput:
    out: GetObjectLockConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_object_lock_configuration = el.find("ObjectLockConfiguration")
    if child_object_lock_configuration is not None:
        import aws_sdk_s3.types.object_lock_configuration

        out["object_lock_configuration"] = (
            aws_sdk_s3.types.object_lock_configuration.deserialize_xml(
                child_object_lock_configuration
            )
        )
    return out
