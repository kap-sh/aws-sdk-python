"""Generated from Smithy shape ``com.amazonaws.iam#CreateVirtualMFADeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.path_type
    import aws_sdk_iam.types.tag_list_type
    import aws_sdk_iam.types.virtual_mfa_device_name


class CreateVirtualMFADeviceRequest(TypedDict):
    path: NotRequired["aws_sdk_iam.types.path_type.pathType"]
    """<p> The path for the virtual MFA device. For more information about paths, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html\">IAM identifiers</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. If it is not included, it defaults to a slash (/).</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007f</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    virtual_mfa_device_name: (
        "aws_sdk_iam.types.virtual_mfa_device_name.virtualMFADeviceName"
    )
    """<p>The name of the virtual MFA device, which must be unique. Use with path to uniquely identify a virtual MFA device.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that you want to attach to the new IAM virtual MFA device. Each tag consists of a key name and an associated value. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p> <note> <p>If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateVirtualMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "path" in value:
        pairs.append((f"{prefix}.Path", str(value["path"])))
    pairs.append(
        (f"{prefix}.VirtualMFADeviceName", str(value["virtual_mfa_device_name"]))
    )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateVirtualMFADeviceRequest:
    out: CreateVirtualMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_virtual_mfa_device_name = el.find("VirtualMFADeviceName")
    if child_virtual_mfa_device_name is not None:
        out["virtual_mfa_device_name"] = str(child_virtual_mfa_device_name.text or "")
    else:
        raise DeserializationError(
            "CreateVirtualMFADeviceRequest.virtual_mfa_device_name required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
