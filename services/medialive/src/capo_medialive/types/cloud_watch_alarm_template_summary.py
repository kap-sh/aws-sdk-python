"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__integer_min10_max86400
    import capo_medialive.types.__string_max64
    import capo_medialive.types.__string_min0_max1024
    import capo_medialive.types.__string_min1_max255_pattern_s
    import capo_medialive.types.__string_min7_max11_pattern_aws097
    import capo_medialive.types.__string_pattern_arn_medialive_cloudwatch_alarm_template
    import capo_medialive.types.__timestamp_iso8601
    import capo_medialive.types.cloud_watch_alarm_template_comparison_operator
    import capo_medialive.types.cloud_watch_alarm_template_statistic
    import capo_medialive.types.cloud_watch_alarm_template_target_resource_type
    import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data
    import capo_medialive.types.tag_map


class CloudWatchAlarmTemplateSummary(TypedDict, closed=True):
    arn: NotRequired[
        "capo_medialive.types.__string_pattern_arn_medialive_cloudwatch_alarm_template.__stringPatternArnMedialiveCloudwatchAlarmTemplate"
    ]
    """A cloudwatch alarm template's ARN (Amazon Resource Name)"""
    comparison_operator: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator"
    ]
    created_at: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    datapoints_to_alarm: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """The number of datapoints within the evaluation period that must be breaching to trigger the alarm."""
    description: NotRequired[
        "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    evaluation_periods: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """The number of periods over which data is compared to the specified threshold."""
    group_id: NotRequired[
        "capo_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
    ]
    """A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`"""
    id: NotRequired[
        "capo_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
    ]
    """A cloudwatch alarm template's id. AWS provided templates have ids that start with `aws-`"""
    metric_name: NotRequired["capo_medialive.types.__string_max64.__stringMax64"]
    """The name of the metric associated with the alarm. Must be compatible with targetResourceType."""
    modified_at: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    name: NotRequired[
        "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    period: NotRequired[
        "capo_medialive.types.__integer_min10_max86400.__integerMin10Max86400"
    ]
    """The period, in seconds, over which the specified statistic is applied."""
    statistic: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic"
    ]
    tags: NotRequired["capo_medialive.types.tag_map.TagMap"]
    target_resource_type: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType"
    ]
    threshold: NotRequired["capo_medialive.types.__double.__double"]
    """The threshold value to compare with the specified statistic."""
    treat_missing_data: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchAlarmTemplateSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "comparison_operator" in value:
        import capo_medialive.types.cloud_watch_alarm_template_comparison_operator

        out["comparisonOperator"] = (
            capo_medialive.types.cloud_watch_alarm_template_comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "created_at" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["createdAt"] = capo_medialive.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "datapoints_to_alarm" in value:
        out["datapointsToAlarm"] = value["datapoints_to_alarm"]
    if "description" in value:
        out["description"] = value["description"]
    if "evaluation_periods" in value:
        out["evaluationPeriods"] = value["evaluation_periods"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "modified_at" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["modifiedAt"] = capo_medialive.types.__timestamp_iso8601.serialize_json(
            value["modified_at"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "period" in value:
        out["period"] = value["period"]
    if "statistic" in value:
        import capo_medialive.types.cloud_watch_alarm_template_statistic

        out["statistic"] = (
            capo_medialive.types.cloud_watch_alarm_template_statistic.serialize_json(
                value["statistic"]
            )
        )
    if "tags" in value:
        import capo_medialive.types.tag_map

        out["tags"] = capo_medialive.types.tag_map.serialize_json(value["tags"])
    if "target_resource_type" in value:
        import capo_medialive.types.cloud_watch_alarm_template_target_resource_type

        out["targetResourceType"] = (
            capo_medialive.types.cloud_watch_alarm_template_target_resource_type.serialize_json(
                value["target_resource_type"]
            )
        )
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    if "treat_missing_data" in value:
        import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data

        out["treatMissingData"] = (
            capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.serialize_json(
                value["treat_missing_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchAlarmTemplateSummary:
    out: CloudWatchAlarmTemplateSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "comparisonOperator" in data:
        import capo_medialive.types.cloud_watch_alarm_template_comparison_operator

        out["comparison_operator"] = (
            capo_medialive.types.cloud_watch_alarm_template_comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    if "createdAt" in data:
        import capo_medialive.types.__timestamp_iso8601

        out["created_at"] = capo_medialive.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "datapointsToAlarm" in data:
        out["datapoints_to_alarm"] = data["datapointsToAlarm"]
    if "description" in data:
        out["description"] = data["description"]
    if "evaluationPeriods" in data:
        out["evaluation_periods"] = data["evaluationPeriods"]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "id" in data:
        out["id"] = data["id"]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "modifiedAt" in data:
        import capo_medialive.types.__timestamp_iso8601

        out["modified_at"] = capo_medialive.types.__timestamp_iso8601.deserialize_json(
            data["modifiedAt"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "period" in data:
        out["period"] = data["period"]
    if "statistic" in data:
        import capo_medialive.types.cloud_watch_alarm_template_statistic

        out["statistic"] = (
            capo_medialive.types.cloud_watch_alarm_template_statistic.deserialize_json(
                data["statistic"]
            )
        )
    if "tags" in data:
        import capo_medialive.types.tag_map

        out["tags"] = capo_medialive.types.tag_map.deserialize_json(data["tags"])
    if "targetResourceType" in data:
        import capo_medialive.types.cloud_watch_alarm_template_target_resource_type

        out["target_resource_type"] = (
            capo_medialive.types.cloud_watch_alarm_template_target_resource_type.deserialize_json(
                data["targetResourceType"]
            )
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    if "treatMissingData" in data:
        import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data

        out["treat_missing_data"] = (
            capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.deserialize_json(
                data["treatMissingData"]
            )
        )
    return out
