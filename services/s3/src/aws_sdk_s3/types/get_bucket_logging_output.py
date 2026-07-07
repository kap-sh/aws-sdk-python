"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketLoggingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.logging_enabled


class GetBucketLoggingOutput(TypedDict, closed=True):
    logging_enabled: NotRequired["aws_sdk_s3.types.logging_enabled.LoggingEnabled"]


# --- restXml ser/de ---
def serialize_xml(value: GetBucketLoggingOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "logging_enabled" in value:
        import aws_sdk_s3.types.logging_enabled

        aws_sdk_s3.types.logging_enabled.serialize_xml(
            value["logging_enabled"], el, "LoggingEnabled"
        )


def deserialize_xml(el: Element) -> GetBucketLoggingOutput:
    out: GetBucketLoggingOutput = {}  # type: ignore[typeddict-item]
    child_logging_enabled = el.find("LoggingEnabled")
    if child_logging_enabled is not None:
        import aws_sdk_s3.types.logging_enabled

        out["logging_enabled"] = aws_sdk_s3.types.logging_enabled.deserialize_xml(
            child_logging_enabled
        )
    return out
