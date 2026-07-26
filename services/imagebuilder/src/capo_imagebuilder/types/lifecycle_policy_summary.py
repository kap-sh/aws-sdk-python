"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.lifecycle_policy_arn
    import capo_imagebuilder.types.lifecycle_policy_resource_type
    import capo_imagebuilder.types.lifecycle_policy_status
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map


class LifecyclePolicySummary(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"]
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy summary resource.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the lifecycle policy.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Optional description for the lifecycle policy.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
    ]
    """<p>The lifecycle policy resource status.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to run the lifecycle policy.</p>"""
    resource_type: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType"
    ]
    """<p>The type of resources the lifecycle policy targets.</p>"""
    date_created: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when Image Builder created the lifecycle policy resource.</p>"""
    date_updated: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when Image Builder updated the lifecycle policy resource.</p>"""
    date_last_run: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp for the last time Image Builder ran the lifecycle policy.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>To help manage your lifecycle policy resources, you can assign your own metadata to each resource in the form of tags. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicySummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_imagebuilder.types.lifecycle_policy_status

        out["status"] = capo_imagebuilder.types.lifecycle_policy_status.serialize_json(
            value["status"]
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "resource_type" in value:
        import capo_imagebuilder.types.lifecycle_policy_resource_type

        out["resourceType"] = (
            capo_imagebuilder.types.lifecycle_policy_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "date_created" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["dateCreated"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["date_created"]
        )
    if "date_updated" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["dateUpdated"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["date_updated"]
        )
    if "date_last_run" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["dateLastRun"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["date_last_run"]
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> LifecyclePolicySummary:
    out: LifecyclePolicySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_policy_status.deserialize_json(
                data["status"]
            )
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "resourceType" in data:
        import capo_imagebuilder.types.lifecycle_policy_resource_type

        out["resource_type"] = (
            capo_imagebuilder.types.lifecycle_policy_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "dateCreated" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["date_created"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["dateCreated"]
            )
        )
    if "dateUpdated" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["date_updated"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["dateUpdated"]
            )
        )
    if "dateLastRun" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["date_last_run"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["dateLastRun"]
            )
        )
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
