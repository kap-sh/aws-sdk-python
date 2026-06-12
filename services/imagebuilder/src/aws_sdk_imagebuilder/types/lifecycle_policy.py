"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time_timestamp
    import aws_sdk_imagebuilder.types.lifecycle_policy_arn
    import aws_sdk_imagebuilder.types.lifecycle_policy_details
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type
    import aws_sdk_imagebuilder.types.lifecycle_policy_status
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.role_name_or_arn
    import aws_sdk_imagebuilder.types.tag_map


class LifecyclePolicy(TypedDict):
    arn: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy resource.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the lifecycle policy.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Optional description for the lifecycle policy.</p>"""
    status: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
    ]
    """<p>Indicates whether the lifecycle policy resource is enabled.</p>"""
    execution_role: NotRequired[
        "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to run the lifecycle policy. This is a custom role that you create.</p>"""
    resource_type: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType"
    ]
    """<p>The type of resources the lifecycle policy targets.</p>"""
    policy_details: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails"
    ]
    """<p>The configuration details for a lifecycle policy resource.</p>"""
    resource_selection: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection"
    ]
    """<p>Resource selection criteria used to run the lifecycle policy.</p>"""
    date_created: NotRequired[
        "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when Image Builder created the lifecycle policy resource.</p>"""
    date_updated: NotRequired[
        "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when Image Builder updated the lifecycle policy resource.</p>"""
    date_last_run: NotRequired[
        "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp for the last time Image Builder ran the lifecycle policy.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>To help manage your lifecycle policy resources, you can assign your own metadata to each resource in the form of tags. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicy) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_status.serialize_json(
                value["status"]
            )
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "resource_type" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type

        out["resourceType"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "policy_details" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_details

        out["policyDetails"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_details.serialize_json(
                value["policy_details"]
            )
        )
    if "resource_selection" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection

        out["resourceSelection"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.serialize_json(
                value["resource_selection"]
            )
        )
    if "date_created" in value:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["dateCreated"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.serialize_json(
                value["date_created"]
            )
        )
    if "date_updated" in value:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["dateUpdated"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.serialize_json(
                value["date_updated"]
            )
        )
    if "date_last_run" in value:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["dateLastRun"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.serialize_json(
                value["date_last_run"]
            )
        )
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> LifecyclePolicy:
    out: LifecyclePolicy = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_status.deserialize_json(
                data["status"]
            )
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "resourceType" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type

        out["resource_type"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "policyDetails" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_details

        out["policy_details"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_details.deserialize_json(
                data["policyDetails"]
            )
        )
    if "resourceSelection" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection

        out["resource_selection"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.deserialize_json(
                data["resourceSelection"]
            )
        )
    if "dateCreated" in data:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["date_created"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["dateCreated"]
            )
        )
    if "dateUpdated" in data:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["date_updated"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["dateUpdated"]
            )
        )
    if "dateLastRun" in data:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["date_last_run"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["dateLastRun"]
            )
        )
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
