"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.base62_id
    import aws_sdk_fms.types.description
    import aws_sdk_fms.types.name
    import aws_sdk_fms.types.resource_set_status
    import aws_sdk_fms.types.time_stamp


class ResourceSetSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_fms.types.base62_id.Base62Id"]
    """<p>A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    name: NotRequired["aws_sdk_fms.types.name.Name"]
    """<p>The descriptive name of the resource set. You can't change the name of a resource set after you create it.</p>"""
    description: NotRequired["aws_sdk_fms.types.description.Description"]
    """<p>A description of the resource set.</p>"""
    last_update_time: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>The last time that the resource set was changed.</p>"""
    resource_set_status: NotRequired[
        "aws_sdk_fms.types.resource_set_status.ResourceSetStatus"
    ]
    """<p>Indicates whether the resource set is in or out of an admin's Region scope.</p> <ul> <li> <p> <code>ACTIVE</code> - The administrator can manage and delete the resource set.</p> </li> <li> <p> <code>OUT_OF_ADMIN_SCOPE</code> - The administrator can view the resource set, but they can't edit or delete the resource set. Existing protections stay in place. Any new resource that come into scope of the resource set won't be protected.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "last_update_time" in value:
        import aws_sdk_fms.types.time_stamp

        out["LastUpdateTime"] = aws_sdk_fms.types.time_stamp.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    if "resource_set_status" in value:
        import aws_sdk_fms.types.resource_set_status

        out["ResourceSetStatus"] = (
            aws_sdk_fms.types.resource_set_status.serialize_aws_json_1_1(
                value["resource_set_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceSetSummary:
    out: ResourceSetSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastUpdateTime" in data:
        import aws_sdk_fms.types.time_stamp

        out["last_update_time"] = aws_sdk_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["LastUpdateTime"]
        )
    if "ResourceSetStatus" in data:
        import aws_sdk_fms.types.resource_set_status

        out["resource_set_status"] = (
            aws_sdk_fms.types.resource_set_status.deserialize_aws_json_1_1(
                data["ResourceSetStatus"]
            )
        )
    return out
