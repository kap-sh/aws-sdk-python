"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateCloudWatchAlarmTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__integer_min10_max86400
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_max64
    import aws_sdk_medialive.types.__string_min0_max1024
    import aws_sdk_medialive.types.__string_min1_max255_pattern_s
    import aws_sdk_medialive.types.__string_pattern_s
    import aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator
    import aws_sdk_medialive.types.cloud_watch_alarm_template_statistic
    import aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type
    import aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data


class UpdateCloudWatchAlarmTemplateRequest(TypedDict, closed=True):
    comparison_operator: NotRequired[
        "aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator"
    ]
    datapoints_to_alarm: NotRequired[
        "aws_sdk_medialive.types.__integer_min1.__integerMin1"
    ]
    """The number of datapoints within the evaluation period that must be breaching to trigger the alarm."""
    description: NotRequired[
        "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    evaluation_periods: NotRequired[
        "aws_sdk_medialive.types.__integer_min1.__integerMin1"
    ]
    """The number of periods over which data is compared to the specified threshold."""
    group_identifier: NotRequired[
        "aws_sdk_medialive.types.__string_pattern_s.__stringPatternS"
    ]
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A cloudwatch alarm template's identifier. Can be either be its id or current name."""
    metric_name: NotRequired["aws_sdk_medialive.types.__string_max64.__stringMax64"]
    """The name of the metric associated with the alarm. Must be compatible with targetResourceType."""
    name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    period: NotRequired[
        "aws_sdk_medialive.types.__integer_min10_max86400.__integerMin10Max86400"
    ]
    """The period, in seconds, over which the specified statistic is applied."""
    statistic: NotRequired[
        "aws_sdk_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic"
    ]
    target_resource_type: NotRequired[
        "aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType"
    ]
    threshold: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """The threshold value to compare with the specified statistic."""
    treat_missing_data: NotRequired[
        "aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCloudWatchAlarmTemplateRequest) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator

        out["comparisonOperator"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "datapoints_to_alarm" in value:
        out["datapointsToAlarm"] = value["datapoints_to_alarm"]
    if "description" in value:
        out["description"] = value["description"]
    if "evaluation_periods" in value:
        out["evaluationPeriods"] = value["evaluation_periods"]
    if "group_identifier" in value:
        out["groupIdentifier"] = value["group_identifier"]
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "period" in value:
        out["period"] = value["period"]
    if "statistic" in value:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_statistic

        out["statistic"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_statistic.serialize_json(
                value["statistic"]
            )
        )
    if "target_resource_type" in value:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type

        out["targetResourceType"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type.serialize_json(
                value["target_resource_type"]
            )
        )
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    if "treat_missing_data" in value:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data

        out["treatMissingData"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data.serialize_json(
                value["treat_missing_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCloudWatchAlarmTemplateRequest:
    out: UpdateCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
    if "comparisonOperator" in data:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator

        out["comparison_operator"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    if "datapointsToAlarm" in data:
        out["datapoints_to_alarm"] = data["datapointsToAlarm"]
    if "description" in data:
        out["description"] = data["description"]
    if "evaluationPeriods" in data:
        out["evaluation_periods"] = data["evaluationPeriods"]
    if "groupIdentifier" in data:
        out["group_identifier"] = data["groupIdentifier"]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "name" in data:
        out["name"] = data["name"]
    if "period" in data:
        out["period"] = data["period"]
    if "statistic" in data:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_statistic

        out["statistic"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_statistic.deserialize_json(
                data["statistic"]
            )
        )
    if "targetResourceType" in data:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type

        out["target_resource_type"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type.deserialize_json(
                data["targetResourceType"]
            )
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    if "treatMissingData" in data:
        import aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data

        out["treat_missing_data"] = (
            aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data.deserialize_json(
                data["treatMissingData"]
            )
        )
    return out
