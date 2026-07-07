"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectEncryptionFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.dssekms_filter
    import aws_sdk_s3_control.types.not_sse_filter
    import aws_sdk_s3_control.types.ssec_filter
    import aws_sdk_s3_control.types.ssekms_filter
    import aws_sdk_s3_control.types.sses3_filter


class _ObjectEncryptionFilter_SSES3(TypedDict, closed=True):
    SSES3: "aws_sdk_s3_control.types.sses3_filter.SSES3Filter"


class _ObjectEncryptionFilter_SSEKMS(TypedDict, closed=True):
    SSEKMS: "aws_sdk_s3_control.types.ssekms_filter.SSEKMSFilter"


class _ObjectEncryptionFilter_DSSEKMS(TypedDict, closed=True):
    DSSEKMS: "aws_sdk_s3_control.types.dssekms_filter.DSSEKMSFilter"


class _ObjectEncryptionFilter_SSEC(TypedDict, closed=True):
    SSEC: "aws_sdk_s3_control.types.ssec_filter.SSECFilter"


class _ObjectEncryptionFilter_NOTSSE(TypedDict, closed=True):
    NOTSSE: "aws_sdk_s3_control.types.not_sse_filter.NotSSEFilter"


ObjectEncryptionFilter: TypeAlias = (
    _ObjectEncryptionFilter_SSES3
    | _ObjectEncryptionFilter_SSEKMS
    | _ObjectEncryptionFilter_DSSEKMS
    | _ObjectEncryptionFilter_SSEC
    | _ObjectEncryptionFilter_NOTSSE
)


# --- restXml ser/de ---
def serialize_xml(value: ObjectEncryptionFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "SSES3" in value:
        import aws_sdk_s3_control.types.sses3_filter

        aws_sdk_s3_control.types.sses3_filter.serialize_xml(
            value["SSES3"], el, "SSE-S3"
        )
    elif "SSEKMS" in value:
        import aws_sdk_s3_control.types.ssekms_filter

        aws_sdk_s3_control.types.ssekms_filter.serialize_xml(
            value["SSEKMS"], el, "SSE-KMS"
        )
    elif "DSSEKMS" in value:
        import aws_sdk_s3_control.types.dssekms_filter

        aws_sdk_s3_control.types.dssekms_filter.serialize_xml(
            value["DSSEKMS"], el, "DSSE-KMS"
        )
    elif "SSEC" in value:
        import aws_sdk_s3_control.types.ssec_filter

        aws_sdk_s3_control.types.ssec_filter.serialize_xml(value["SSEC"], el, "SSE-C")
    elif "NOTSSE" in value:
        import aws_sdk_s3_control.types.not_sse_filter

        aws_sdk_s3_control.types.not_sse_filter.serialize_xml(
            value["NOTSSE"], el, "NOT-SSE"
        )
    else:
        raise SerializationError("ObjectEncryptionFilter: no variant present")


def deserialize_xml(el: Element) -> ObjectEncryptionFilter:
    for child in el:
        if child.tag == "SSE-S3":
            import aws_sdk_s3_control.types.sses3_filter

            return {
                "SSES3": aws_sdk_s3_control.types.sses3_filter.deserialize_xml(child)
            }
        elif child.tag == "SSE-KMS":
            import aws_sdk_s3_control.types.ssekms_filter

            return {
                "SSEKMS": aws_sdk_s3_control.types.ssekms_filter.deserialize_xml(child)
            }
        elif child.tag == "DSSE-KMS":
            import aws_sdk_s3_control.types.dssekms_filter

            return {
                "DSSEKMS": aws_sdk_s3_control.types.dssekms_filter.deserialize_xml(
                    child
                )
            }
        elif child.tag == "SSE-C":
            import aws_sdk_s3_control.types.ssec_filter

            return {"SSEC": aws_sdk_s3_control.types.ssec_filter.deserialize_xml(child)}
        elif child.tag == "NOT-SSE":
            import aws_sdk_s3_control.types.not_sse_filter

            return {
                "NOTSSE": aws_sdk_s3_control.types.not_sse_filter.deserialize_xml(child)
            }
    raise DeserializationError("ObjectEncryptionFilter: no recognized variant element")
