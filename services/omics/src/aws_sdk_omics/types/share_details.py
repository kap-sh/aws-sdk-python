"""Generated from Smithy shape ``com.amazonaws.omics#ShareDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.share_name
    import aws_sdk_omics.types.share_status
    import aws_sdk_omics.types.status_message
    import aws_sdk_omics.types.update_time


class ShareDetails(TypedDict):
    share_id: NotRequired["str"]
    """<p>The ID of the resource share.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Arn of the shared resource. </p>"""
    resource_id: NotRequired["str"]
    """<p>The ID of the shared resource. </p>"""
    principal_subscriber: NotRequired["str"]
    """<p>The principal subscriber is the account that is sharing the resource.</p>"""
    owner_id: NotRequired["str"]
    """<p>The account ID for the data owner. The owner creates the resource share.</p>"""
    status: NotRequired["aws_sdk_omics.types.share_status.ShareStatus"]
    """<p>The status of the share.</p>"""
    status_message: NotRequired["aws_sdk_omics.types.status_message.StatusMessage"]
    """<p>The status message for a resource share. It provides additional details about the share status.</p>"""
    share_name: NotRequired["aws_sdk_omics.types.share_name.ShareName"]
    """<p>The name of the resource share.</p>"""
    creation_time: NotRequired["aws_sdk_omics.types.creation_time.CreationTime"]
    """<p>The timestamp of when the resource share was created.</p>"""
    update_time: NotRequired["aws_sdk_omics.types.update_time.UpdateTime"]
    """<p>The timestamp of the resource share update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareDetails) -> dict:
    out: dict = {}
    if "share_id" in value:
        out["shareId"] = value["share_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "principal_subscriber" in value:
        out["principalSubscriber"] = value["principal_subscriber"]
    if "owner_id" in value:
        out["ownerId"] = value["owner_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "share_name" in value:
        out["shareName"] = value["share_name"]
    if "creation_time" in value:
        import aws_sdk_omics.types.creation_time

        out["creationTime"] = aws_sdk_omics.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "update_time" in value:
        import aws_sdk_omics.types.update_time

        out["updateTime"] = aws_sdk_omics.types.update_time.serialize_json(
            value["update_time"]
        )
    return out


def deserialize_json(data: dict) -> ShareDetails:
    out: ShareDetails = {}  # type: ignore[typeddict-item]
    if "shareId" in data:
        out["share_id"] = data["shareId"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "principalSubscriber" in data:
        out["principal_subscriber"] = data["principalSubscriber"]
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "shareName" in data:
        out["share_name"] = data["shareName"]
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    if "updateTime" in data:
        import aws_sdk_omics.types.update_time

        out["update_time"] = aws_sdk_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    return out
