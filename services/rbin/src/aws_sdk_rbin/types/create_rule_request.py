"""Generated from Smithy shape ``com.amazonaws.rbin#CreateRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rbin.types.description
    import aws_sdk_rbin.types.exclude_resource_tags
    import aws_sdk_rbin.types.lock_configuration
    import aws_sdk_rbin.types.resource_tags
    import aws_sdk_rbin.types.resource_type
    import aws_sdk_rbin.types.retention_period
    import aws_sdk_rbin.types.tag_list


class CreateRuleRequest(TypedDict):
    retention_period: "aws_sdk_rbin.types.retention_period.RetentionPeriod"
    """<p>Information about the retention period for which the retention rule is to retain resources.</p>"""
    description: NotRequired["aws_sdk_rbin.types.description.Description"]
    """<p>The retention rule description.</p>"""
    tags: NotRequired["aws_sdk_rbin.types.tag_list.TagList"]
    """<p>Information about the tags to assign to the retention rule.</p>"""
    resource_type: "aws_sdk_rbin.types.resource_type.ResourceType"
    """<p>The resource type to be retained by the retention rule. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.</p> <ul> <li> <p>To retain EBS volumes, specify <code>EBS_VOLUME</code>.</p> </li> <li> <p>To retain EBS snapshots, specify <code>EBS_SNAPSHOT</code> </p> </li> <li> <p>To retain EBS-backed AMIs, specify <code>EC2_IMAGE</code>.</p> </li> </ul>"""
    resource_tags: NotRequired["aws_sdk_rbin.types.resource_tags.ResourceTags"]
    """<p>[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.</p> <p>You can add the same tag key and value pair to a maximum or five retention rules.</p> <p>To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.</p>"""
    lock_configuration: NotRequired[
        "aws_sdk_rbin.types.lock_configuration.LockConfiguration"
    ]
    """<p>Information about the retention rule lock configuration.</p>"""
    exclude_resource_tags: NotRequired[
        "aws_sdk_rbin.types.exclude_resource_tags.ExcludeResourceTags"
    ]
    """<p>[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.</p> <p>You can't specify exclusion tags for tag-level retention rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_rbin.types.retention_period

    out["RetentionPeriod"] = aws_sdk_rbin.types.retention_period.serialize_json(
        value["retention_period"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_rbin.types.tag_list

        out["Tags"] = aws_sdk_rbin.types.tag_list.serialize_json(value["tags"])
    import aws_sdk_rbin.types.resource_type

    out["ResourceType"] = aws_sdk_rbin.types.resource_type.serialize_json(
        value["resource_type"]
    )
    if "resource_tags" in value:
        import aws_sdk_rbin.types.resource_tags

        out["ResourceTags"] = aws_sdk_rbin.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    if "lock_configuration" in value:
        import aws_sdk_rbin.types.lock_configuration

        out["LockConfiguration"] = aws_sdk_rbin.types.lock_configuration.serialize_json(
            value["lock_configuration"]
        )
    if "exclude_resource_tags" in value:
        import aws_sdk_rbin.types.exclude_resource_tags

        out["ExcludeResourceTags"] = (
            aws_sdk_rbin.types.exclude_resource_tags.serialize_json(
                value["exclude_resource_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRuleRequest:
    out: CreateRuleRequest = {}  # type: ignore[typeddict-item]
    if "RetentionPeriod" in data:
        import aws_sdk_rbin.types.retention_period

        out["retention_period"] = aws_sdk_rbin.types.retention_period.deserialize_json(
            data["RetentionPeriod"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.retention_period required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_rbin.types.tag_list

        out["tags"] = aws_sdk_rbin.types.tag_list.deserialize_json(data["Tags"])
    if "ResourceType" in data:
        import aws_sdk_rbin.types.resource_type

        out["resource_type"] = aws_sdk_rbin.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.resource_type required")
    if "ResourceTags" in data:
        import aws_sdk_rbin.types.resource_tags

        out["resource_tags"] = aws_sdk_rbin.types.resource_tags.deserialize_json(
            data["ResourceTags"]
        )
    if "LockConfiguration" in data:
        import aws_sdk_rbin.types.lock_configuration

        out["lock_configuration"] = (
            aws_sdk_rbin.types.lock_configuration.deserialize_json(
                data["LockConfiguration"]
            )
        )
    if "ExcludeResourceTags" in data:
        import aws_sdk_rbin.types.exclude_resource_tags

        out["exclude_resource_tags"] = (
            aws_sdk_rbin.types.exclude_resource_tags.deserialize_json(
                data["ExcludeResourceTags"]
            )
        )
    return out
