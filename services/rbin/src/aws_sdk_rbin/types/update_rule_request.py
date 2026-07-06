"""Generated from Smithy shape ``com.amazonaws.rbin#UpdateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rbin.types.description
    import aws_sdk_rbin.types.exclude_resource_tags
    import aws_sdk_rbin.types.resource_tags
    import aws_sdk_rbin.types.resource_type
    import aws_sdk_rbin.types.retention_period
    import aws_sdk_rbin.types.rule_identifier


class UpdateRuleRequest(TypedDict, closed=True):
    identifier: "aws_sdk_rbin.types.rule_identifier.RuleIdentifier"
    """<p>The unique ID of the retention rule.</p>"""
    retention_period: NotRequired["aws_sdk_rbin.types.retention_period.RetentionPeriod"]
    """<p>Information about the retention period for which the retention rule is to retain resources.</p>"""
    description: NotRequired["aws_sdk_rbin.types.description.Description"]
    """<p>The retention rule description.</p>"""
    resource_type: NotRequired["aws_sdk_rbin.types.resource_type.ResourceType"]
    """<note> <p>This parameter is currently not supported. You can't update a retention rule's resource type after creation.</p> </note>"""
    resource_tags: NotRequired["aws_sdk_rbin.types.resource_tags.ResourceTags"]
    """<p>[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.</p> <p>You can add the same tag key and value pair to a maximum or five retention rules.</p> <p>To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.</p>"""
    exclude_resource_tags: NotRequired[
        "aws_sdk_rbin.types.exclude_resource_tags.ExcludeResourceTags"
    ]
    """<p>[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.</p> <p>You can't specify exclusion tags for tag-level retention rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleRequest) -> dict:
    out: dict = {}
    if "retention_period" in value:
        import aws_sdk_rbin.types.retention_period

        out["RetentionPeriod"] = aws_sdk_rbin.types.retention_period.serialize_json(
            value["retention_period"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "resource_type" in value:
        import aws_sdk_rbin.types.resource_type

        out["ResourceType"] = aws_sdk_rbin.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "resource_tags" in value:
        import aws_sdk_rbin.types.resource_tags

        out["ResourceTags"] = aws_sdk_rbin.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    if "exclude_resource_tags" in value:
        import aws_sdk_rbin.types.exclude_resource_tags

        out["ExcludeResourceTags"] = (
            aws_sdk_rbin.types.exclude_resource_tags.serialize_json(
                value["exclude_resource_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRuleRequest:
    out: UpdateRuleRequest = {}  # type: ignore[typeddict-item]
    if "RetentionPeriod" in data:
        import aws_sdk_rbin.types.retention_period

        out["retention_period"] = aws_sdk_rbin.types.retention_period.deserialize_json(
            data["RetentionPeriod"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ResourceType" in data:
        import aws_sdk_rbin.types.resource_type

        out["resource_type"] = aws_sdk_rbin.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    if "ResourceTags" in data:
        import aws_sdk_rbin.types.resource_tags

        out["resource_tags"] = aws_sdk_rbin.types.resource_tags.deserialize_json(
            data["ResourceTags"]
        )
    if "ExcludeResourceTags" in data:
        import aws_sdk_rbin.types.exclude_resource_tags

        out["exclude_resource_tags"] = (
            aws_sdk_rbin.types.exclude_resource_tags.deserialize_json(
                data["ExcludeResourceTags"]
            )
        )
    return out
