"""Generated from Smithy shape ``com.amazonaws.medialive#CreateCloudWatchAlarmTemplateGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_min0_max1024
    import aws_sdk_medialive.types.__string_min1_max255_pattern_s
    import aws_sdk_medialive.types.__string_min7_max11_pattern_aws097
    import aws_sdk_medialive.types.__string_pattern_arn_medialive_cloudwatch_alarm_template_group
    import aws_sdk_medialive.types.__timestamp_iso8601
    import aws_sdk_medialive.types.tag_map


class CreateCloudWatchAlarmTemplateGroupResponse(TypedDict):
    arn: NotRequired[
        "aws_sdk_medialive.types.__string_pattern_arn_medialive_cloudwatch_alarm_template_group.__stringPatternArnMedialiveCloudwatchAlarmTemplateGroup"
    ]
    """A cloudwatch alarm template group's ARN (Amazon Resource Name)"""
    created_at: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    description: NotRequired[
        "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    id: NotRequired[
        "aws_sdk_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
    ]
    """A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`"""
    modified_at: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    tags: NotRequired["aws_sdk_medialive.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudWatchAlarmTemplateGroupResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "modified_at" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["modifiedAt"] = aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
            value["modified_at"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCloudWatchAlarmTemplateGroupResponse:
    out: CreateCloudWatchAlarmTemplateGroupResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["created_at"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["createdAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "modifiedAt" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["modified_at"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.deserialize_json(data["tags"])
    return out
