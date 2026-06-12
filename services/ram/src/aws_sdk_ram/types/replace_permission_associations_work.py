"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWork``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.replace_permission_associations_work_status
    import aws_sdk_ram.types.string


class ReplacePermissionAssociationsWork(TypedDict):
    id: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The unique identifier for the background task associated with one <a>ReplacePermissionAssociations</a> request.</p>"""
    from_permission_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the managed permission that this background task is replacing.</p>"""
    from_permission_version: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The version of the managed permission that this background task is replacing.</p>"""
    to_permission_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The ARN of the managed permission that this background task is associating with the resource shares in place of the managed permission and version specified in <code>fromPermissionArn</code> and <code>fromPermissionVersion</code>.</p>"""
    to_permission_version: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The version of the managed permission that this background task is associating with the resource shares. This is always the version that is currently the default for this managed permission.</p>"""
    status: NotRequired[
        "aws_sdk_ram.types.replace_permission_associations_work_status.ReplacePermissionAssociationsWorkStatus"
    ]
    """<p>Specifies the current status of the background tasks for the specified ID. The output is one of the following strings:</p> <ul> <li> <p> <code>IN_PROGRESS</code> </p> </li> <li> <p> <code>COMPLETED</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> </ul>"""
    status_message: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies the reason for a <code>FAILED</code> status. This field is present only when there <code>status</code> is <code>FAILED</code>.</p>"""
    creation_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when this asynchronous background task was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the status of this background task was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsWork) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "from_permission_arn" in value:
        out["fromPermissionArn"] = value["from_permission_arn"]
    if "from_permission_version" in value:
        out["fromPermissionVersion"] = value["from_permission_version"]
    if "to_permission_arn" in value:
        out["toPermissionArn"] = value["to_permission_arn"]
    if "to_permission_version" in value:
        out["toPermissionVersion"] = value["to_permission_version"]
    if "status" in value:
        import aws_sdk_ram.types.replace_permission_associations_work_status

        out["status"] = (
            aws_sdk_ram.types.replace_permission_associations_work_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_time" in value:
        import aws_sdk_ram.types.date_time

        out["creationTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_ram.types.date_time

        out["lastUpdatedTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> ReplacePermissionAssociationsWork:
    out: ReplacePermissionAssociationsWork = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "fromPermissionArn" in data:
        out["from_permission_arn"] = data["fromPermissionArn"]
    if "fromPermissionVersion" in data:
        out["from_permission_version"] = data["fromPermissionVersion"]
    if "toPermissionArn" in data:
        out["to_permission_arn"] = data["toPermissionArn"]
    if "toPermissionVersion" in data:
        out["to_permission_version"] = data["toPermissionVersion"]
    if "status" in data:
        import aws_sdk_ram.types.replace_permission_associations_work_status

        out["status"] = (
            aws_sdk_ram.types.replace_permission_associations_work_status.deserialize_json(
                data["status"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationTime" in data:
        import aws_sdk_ram.types.date_time

        out["creation_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_ram.types.date_time

        out["last_updated_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    return out
