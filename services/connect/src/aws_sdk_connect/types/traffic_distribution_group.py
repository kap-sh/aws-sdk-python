"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.description250
    import aws_sdk_connect.types.instance_arn
    import aws_sdk_connect.types.name128
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.traffic_distribution_group_arn
    import aws_sdk_connect.types.traffic_distribution_group_id
    import aws_sdk_connect.types.traffic_distribution_group_status


class TrafficDistributionGroup(TypedDict):
    id: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_id.TrafficDistributionGroupId"
    ]
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.</p>"""
    arn: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_arn.TrafficDistributionGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the traffic distribution group.</p>"""
    name: NotRequired["aws_sdk_connect.types.name128.Name128"]
    """<p>The name of the traffic distribution group.</p>"""
    description: NotRequired["aws_sdk_connect.types.description250.Description250"]
    """<p>The description of the traffic distribution group.</p>"""
    instance_arn: NotRequired["aws_sdk_connect.types.instance_arn.InstanceArn"]
    """<p>The Amazon Resource Name (ARN).</p>"""
    status: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_status.TrafficDistributionGroupStatus"
    ]
    """<p>The status of the traffic distribution group.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> means the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html\">CreateTrafficDistributionGroup</a> operation is still in progress and has not yet completed.</p> </li> <li> <p> <code>ACTIVE</code> means the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html\">CreateTrafficDistributionGroup</a> operation has succeeded.</p> </li> <li> <p> <code>CREATION_FAILED</code> indicates that the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html\">CreateTrafficDistributionGroup</a> operation has failed.</p> </li> <li> <p> <code>PENDING_DELETION</code> means the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html\">DeleteTrafficDistributionGroup</a> operation is still in progress and has not yet completed.</p> </li> <li> <p> <code>DELETION_FAILED</code> means the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html\">DeleteTrafficDistributionGroup</a> operation has failed.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> means the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html\">UpdateTrafficDistribution</a> operation is still in progress and has not yet completed.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    is_default: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether this is the default traffic distribution group created during instance replication. The default traffic distribution group cannot be deleted by the <code>DeleteTrafficDistributionGroup</code> API. The default traffic distribution group is deleted as part of the process for deleting a replica.</p> <note> <p>The <code>SignInConfig</code> distribution is available only on a default <code>TrafficDistributionGroup</code> (see the <code>IsDefault</code> parameter in the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html\">TrafficDistributionGroup</a> data type). If you call <code>UpdateTrafficDistribution</code> with a modified <code>SignInConfig</code> and a non-default <code>TrafficDistributionGroup</code>, an <code>InvalidRequestException</code> is returned.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficDistributionGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "status" in value:
        import aws_sdk_connect.types.traffic_distribution_group_status

        out["Status"] = (
            aws_sdk_connect.types.traffic_distribution_group_status.serialize_json(
                value["status"]
            )
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    out["IsDefault"] = value.get("is_default", False)
    return out


def deserialize_json(data: dict) -> TrafficDistributionGroup:
    out: TrafficDistributionGroup = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "Status" in data:
        import aws_sdk_connect.types.traffic_distribution_group_status

        out["status"] = (
            aws_sdk_connect.types.traffic_distribution_group_status.deserialize_json(
                data["Status"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    return out
