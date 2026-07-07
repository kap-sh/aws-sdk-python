"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.base62_id
    import aws_sdk_fms.types.description
    import aws_sdk_fms.types.name
    import aws_sdk_fms.types.resource_set_status
    import aws_sdk_fms.types.resource_type_list
    import aws_sdk_fms.types.time_stamp
    import aws_sdk_fms.types.update_token


class ResourceSet(TypedDict, closed=True):
    id: NotRequired["aws_sdk_fms.types.base62_id.Base62Id"]
    """<p>A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    name: "aws_sdk_fms.types.name.Name"
    """<p>The descriptive name of the resource set. You can't change the name of a resource set after you create it.</p>"""
    description: NotRequired["aws_sdk_fms.types.description.Description"]
    """<p>A description of the resource set.</p>"""
    update_token: NotRequired["aws_sdk_fms.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Firewall Manager returns a token to your requests that access the resource set. The token marks the state of the resource set resource at the time of the request. Update tokens are not allowed when creating a resource set. After creation, each subsequent update call to the resource set requires the update token. </p> <p>To make an unconditional change to the resource set, omit the token in your update request. Without the token, Firewall Manager performs your updates regardless of whether the resource set has changed since you last retrieved it.</p> <p>To make a conditional change to the resource set, provide the token in your update request. Firewall Manager uses the token to ensure that the resource set hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the resource set again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    resource_type_list: "aws_sdk_fms.types.resource_type_list.ResourceTypeList"
    """<p>Determines the resources that can be associated to the resource set. Depending on your setting for max results and the number of resource sets, a single call might not return the full list.</p>"""
    last_update_time: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>The last time that the resource set was changed.</p>"""
    resource_set_status: NotRequired[
        "aws_sdk_fms.types.resource_set_status.ResourceSetStatus"
    ]
    """<p>Indicates whether the resource set is in or out of an admin's Region scope.</p> <ul> <li> <p> <code>ACTIVE</code> - The administrator can manage and delete the resource set.</p> </li> <li> <p> <code>OUT_OF_ADMIN_SCOPE</code> - The administrator can view the resource set, but they can't edit or delete the resource set. Existing protections stay in place. Any new resource that come into scope of the resource set won't be protected.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    import aws_sdk_fms.types.resource_type_list

    out["ResourceTypeList"] = (
        aws_sdk_fms.types.resource_type_list.serialize_aws_json_1_1(
            value["resource_type_list"]
        )
    )
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


def deserialize_aws_json_1_1(data: dict) -> ResourceSet:
    out: ResourceSet = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ResourceSet.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    if "ResourceTypeList" in data:
        import aws_sdk_fms.types.resource_type_list

        out["resource_type_list"] = (
            aws_sdk_fms.types.resource_type_list.deserialize_aws_json_1_1(
                data["ResourceTypeList"]
            )
        )
    else:
        raise DeserializationError("ResourceSet.resource_type_list required")
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
