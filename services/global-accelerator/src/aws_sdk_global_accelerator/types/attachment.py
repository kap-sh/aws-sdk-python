"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Attachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.attachment_name
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.principals
    import aws_sdk_global_accelerator.types.resources
    import aws_sdk_global_accelerator.types.timestamp


class Attachment(TypedDict, closed=True):
    attachment_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the cross-account attachment.</p>"""
    name: NotRequired["aws_sdk_global_accelerator.types.attachment_name.AttachmentName"]
    """<p>The name of the cross-account attachment.</p>"""
    principals: NotRequired["aws_sdk_global_accelerator.types.principals.Principals"]
    """<p>The principals included in the cross-account attachment.</p>"""
    resources: NotRequired["aws_sdk_global_accelerator.types.resources.Resources"]
    """<p>The resources included in the cross-account attachment.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_global_accelerator.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the cross-account attachment was last modified.</p>"""
    created_time: NotRequired["aws_sdk_global_accelerator.types.timestamp.Timestamp"]
    """<p>The date and time that the cross-account attachment was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attachment) -> dict:
    out: dict = {}
    if "attachment_arn" in value:
        out["AttachmentArn"] = value["attachment_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "principals" in value:
        import aws_sdk_global_accelerator.types.principals

        out["Principals"] = (
            aws_sdk_global_accelerator.types.principals.serialize_aws_json_1_1(
                value["principals"]
            )
        )
    if "resources" in value:
        import aws_sdk_global_accelerator.types.resources

        out["Resources"] = (
            aws_sdk_global_accelerator.types.resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_global_accelerator.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_global_accelerator.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "created_time" in value:
        import aws_sdk_global_accelerator.types.timestamp

        out["CreatedTime"] = (
            aws_sdk_global_accelerator.types.timestamp.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if "AttachmentArn" in data:
        out["attachment_arn"] = data["AttachmentArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Principals" in data:
        import aws_sdk_global_accelerator.types.principals

        out["principals"] = (
            aws_sdk_global_accelerator.types.principals.deserialize_aws_json_1_1(
                data["Principals"]
            )
        )
    if "Resources" in data:
        import aws_sdk_global_accelerator.types.resources

        out["resources"] = (
            aws_sdk_global_accelerator.types.resources.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_global_accelerator.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_global_accelerator.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_global_accelerator.types.timestamp

        out["created_time"] = (
            aws_sdk_global_accelerator.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    return out
