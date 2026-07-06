"""Generated from Smithy shape ``com.amazonaws.iam#TagMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.serial_number_type
    import aws_sdk_iam.types.tag_list_type


class TagMFADeviceRequest(TypedDict, closed=True):
    serial_number: "aws_sdk_iam.types.serial_number_type.serialNumberType"
    r"""<p>The unique identifier for the IAM virtual MFA device to which you want to add tags. For virtual MFA devices, the serial number is the same as the ARN.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "aws_sdk_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM virtual MFA device. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SerialNumber", str(value["serial_number"])))
    import aws_sdk_iam.types.tag_list_type

    aws_sdk_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{prefix}.Tags"
    )


def deserialize_query(el: Element) -> TagMFADeviceRequest:
    out: TagMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("TagMFADeviceRequest.serial_number required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagMFADeviceRequest.tags required")
    return out
