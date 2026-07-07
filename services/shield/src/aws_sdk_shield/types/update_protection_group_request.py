"""Generated from Smithy shape ``com.amazonaws.shield#UpdateProtectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.protected_resource_type
    import aws_sdk_shield.types.protection_group_aggregation
    import aws_sdk_shield.types.protection_group_id
    import aws_sdk_shield.types.protection_group_members
    import aws_sdk_shield.types.protection_group_pattern


class UpdateProtectionGroupRequest(TypedDict, closed=True):
    protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId"
    """<p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>"""
    aggregation: (
        "aws_sdk_shield.types.protection_group_aggregation.ProtectionGroupAggregation"
    )
    """<p>Defines how Shield combines resource data for the group in order to detect, mitigate, and report events.</p> <ul> <li> <p>Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.</p> </li> <li> <p>Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.</p> </li> <li> <p>Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.</p> </li> </ul>"""
    pattern: "aws_sdk_shield.types.protection_group_pattern.ProtectionGroupPattern"
    """<p>The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.</p>"""
    resource_type: NotRequired[
        "aws_sdk_shield.types.protected_resource_type.ProtectedResourceType"
    ]
    """<p>The resource type to include in the protection group. All protected resources of this type are included in the protection group. You must set this when you set <code>Pattern</code> to <code>BY_RESOURCE_TYPE</code> and you must not set it for any other <code>Pattern</code> setting. </p>"""
    members: NotRequired[
        "aws_sdk_shield.types.protection_group_members.ProtectionGroupMembers"
    ]
    """<p>The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set <code>Pattern</code> to <code>ARBITRARY</code> and you must not set it for any other <code>Pattern</code> setting. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProtectionGroupRequest) -> dict:
    out: dict = {}
    out["ProtectionGroupId"] = value["protection_group_id"]
    import aws_sdk_shield.types.protection_group_aggregation

    out["Aggregation"] = (
        aws_sdk_shield.types.protection_group_aggregation.serialize_aws_json_1_1(
            value["aggregation"]
        )
    )
    import aws_sdk_shield.types.protection_group_pattern

    out["Pattern"] = (
        aws_sdk_shield.types.protection_group_pattern.serialize_aws_json_1_1(
            value["pattern"]
        )
    )
    if "resource_type" in value:
        import aws_sdk_shield.types.protected_resource_type

        out["ResourceType"] = (
            aws_sdk_shield.types.protected_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "members" in value:
        import aws_sdk_shield.types.protection_group_members

        out["Members"] = (
            aws_sdk_shield.types.protection_group_members.serialize_aws_json_1_1(
                value["members"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProtectionGroupRequest:
    out: UpdateProtectionGroupRequest = {}  # type: ignore[typeddict-item]
    if "ProtectionGroupId" in data:
        out["protection_group_id"] = data["ProtectionGroupId"]
    else:
        raise DeserializationError(
            "UpdateProtectionGroupRequest.protection_group_id required"
        )
    if "Aggregation" in data:
        import aws_sdk_shield.types.protection_group_aggregation

        out["aggregation"] = (
            aws_sdk_shield.types.protection_group_aggregation.deserialize_aws_json_1_1(
                data["Aggregation"]
            )
        )
    else:
        raise DeserializationError("UpdateProtectionGroupRequest.aggregation required")
    if "Pattern" in data:
        import aws_sdk_shield.types.protection_group_pattern

        out["pattern"] = (
            aws_sdk_shield.types.protection_group_pattern.deserialize_aws_json_1_1(
                data["Pattern"]
            )
        )
    else:
        raise DeserializationError("UpdateProtectionGroupRequest.pattern required")
    if "ResourceType" in data:
        import aws_sdk_shield.types.protected_resource_type

        out["resource_type"] = (
            aws_sdk_shield.types.protected_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "Members" in data:
        import aws_sdk_shield.types.protection_group_members

        out["members"] = (
            aws_sdk_shield.types.protection_group_members.deserialize_aws_json_1_1(
                data["Members"]
            )
        )
    return out
