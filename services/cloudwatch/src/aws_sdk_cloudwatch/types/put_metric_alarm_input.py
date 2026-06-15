"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutMetricAlarmInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.actions_enabled
    import aws_sdk_cloudwatch.types.alarm_description
    import aws_sdk_cloudwatch.types.alarm_name
    import aws_sdk_cloudwatch.types.comparison_operator
    import aws_sdk_cloudwatch.types.datapoints_to_alarm
    import aws_sdk_cloudwatch.types.dimensions
    import aws_sdk_cloudwatch.types.evaluate_low_sample_count_percentile
    import aws_sdk_cloudwatch.types.evaluation_criteria
    import aws_sdk_cloudwatch.types.evaluation_interval
    import aws_sdk_cloudwatch.types.evaluation_periods
    import aws_sdk_cloudwatch.types.extended_statistic
    import aws_sdk_cloudwatch.types.metric_data_queries
    import aws_sdk_cloudwatch.types.metric_id
    import aws_sdk_cloudwatch.types.metric_name
    import aws_sdk_cloudwatch.types.namespace
    import aws_sdk_cloudwatch.types.period
    import aws_sdk_cloudwatch.types.resource_list
    import aws_sdk_cloudwatch.types.standard_unit
    import aws_sdk_cloudwatch.types.statistic
    import aws_sdk_cloudwatch.types.tag_list
    import aws_sdk_cloudwatch.types.threshold
    import aws_sdk_cloudwatch.types.treat_missing_data


class PutMetricAlarmInput(TypedDict):
    alarm_name: NotRequired["aws_sdk_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name for the alarm. This name must be unique within the Region.</p> <p>The name must contain only UTF-8 characters, and can't contain ASCII control characters</p>"""
    alarm_description: NotRequired[
        "aws_sdk_cloudwatch.types.alarm_description.AlarmDescription"
    ]
    """<p>The description for the alarm.</p>"""
    actions_enabled: NotRequired[
        "aws_sdk_cloudwatch.types.actions_enabled.ActionsEnabled"
    ]
    """<p>Indicates whether actions should be executed during any changes to the alarm state. The default is <code>TRUE</code>.</p>"""
    ok_actions: NotRequired["aws_sdk_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to an <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>SNS notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>"""
    alarm_actions: NotRequired["aws_sdk_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>SNS notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul> <p> <b>Start a Amazon Q Developer operational investigation</b> </p> <p> <code>arn:aws:aiops:<i>region</i>:<i>account-id</i>:investigation-group:<i>investigation-group-id</i> </code> </p>"""
    insufficient_data_actions: NotRequired[
        "aws_sdk_cloudwatch.types.resource_list.ResourceList"
    ]
    """<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>SNS notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>"""
    metric_name: NotRequired["aws_sdk_cloudwatch.types.metric_name.MetricName"]
    """<p>The name for the metric associated with the alarm. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code>, a <code>Metrics</code> array, or an <code>EvaluationCriteria</code>.</p> <p>If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the <code>Namespace</code>, <code>Dimensions</code>, <code>Period</code>, <code>Unit</code>, <code>Statistic</code>, or <code>ExtendedStatistic</code> parameters. Instead, you specify all this information in the <code>Metrics</code> array.</p>"""
    namespace: NotRequired["aws_sdk_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace for the metric associated specified in <code>MetricName</code>.</p>"""
    statistic: NotRequired["aws_sdk_cloudwatch.types.statistic.Statistic"]
    """<p>The statistic for the metric specified in <code>MetricName</code>, other than percentile. For percentile statistics, use <code>ExtendedStatistic</code>. When you call <code>PutMetricAlarm</code> and specify a <code>MetricName</code>, you must specify either <code>Statistic</code> or <code>ExtendedStatistic,</code> but not both.</p>"""
    extended_statistic: NotRequired[
        "aws_sdk_cloudwatch.types.extended_statistic.ExtendedStatistic"
    ]
    r"""<p>The extended statistic for the metric specified in <code>MetricName</code>. When you call <code>PutMetricAlarm</code> and specify a <code>MetricName</code>, you must specify either <code>Statistic</code> or <code>ExtendedStatistic</code> but not both.</p> <p>If you specify <code>ExtendedStatistic</code>, the following are valid values:</p> <ul> <li> <p> <code>p90</code> </p> </li> <li> <p> <code>tm90</code> </p> </li> <li> <p> <code>tc90</code> </p> </li> <li> <p> <code>ts90</code> </p> </li> <li> <p> <code>wm90</code> </p> </li> <li> <p> <code>IQM</code> </p> </li> <li> <p> <code>PR(<i>n</i>:<i>m</i>)</code> where n and m are values of the metric</p> </li> <li> <p> <code>TC(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> <li> <p> <code>TM(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> <li> <p> <code>TS(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> <li> <p> <code>WM(<i>X</i>%:<i>X</i>%)</code> where X is between 10 and 90 inclusive.</p> </li> </ul> <p>For more information about these extended statistics, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html\">CloudWatch statistics definitions</a>.</p>"""
    dimensions: NotRequired["aws_sdk_cloudwatch.types.dimensions.Dimensions"]
    """<p>The dimensions for the metric specified in <code>MetricName</code>.</p>"""
    period: NotRequired["aws_sdk_cloudwatch.types.period.Period"]
    r"""<p>The length, in seconds, used each time the metric specified in <code>MetricName</code> is evaluated. Valid values are 10, 20, 30, and any multiple of 60.</p> <p> <code>Period</code> is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the <code>Metrics</code> array.</p> <p>Be sure to specify 10, 20, or 30 only for metrics that are stored by a <code>PutMetricData</code> call with a <code>StorageResolution</code> of 1. If you specify a period of 10, 20, or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm might often lapse into INSUFFICENT_DATA status. Specifying 10, 20, or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see <a href=\"https://aws.amazon.com/cloudwatch/pricing/\">Amazon CloudWatch Pricing</a>.</p> <p>An alarm's total current evaluation period can be no longer than seven days, so <code>Period</code> multiplied by <code>EvaluationPeriods</code> can't be more than 604,800 seconds. For alarms with a period of less than one hour (3,600 seconds), the total evaluation period can't be longer than one day (86,400 seconds).</p>"""
    unit: NotRequired["aws_sdk_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately. If you are creating an alarm based on a metric math expression, you can specify the unit for each metric (if needed) within the objects in the <code>Metrics</code> array.</p> <p>If you don't specify <code>Unit</code>, CloudWatch retrieves all unit types that have been published for the metric and attempts to evaluate the alarm. Usually, metrics are published with only one unit, so the alarm works as intended.</p> <p>However, if the metric is published with multiple types of units and you don't specify a unit, the alarm's behavior is not defined and it behaves unpredictably.</p> <p>We recommend omitting <code>Unit</code> so that you don't inadvertently specify an incorrect unit that is not published for this metric. Doing so causes the alarm to be stuck in the <code>INSUFFICIENT DATA</code> state.</p>"""
    evaluation_periods: NotRequired[
        "aws_sdk_cloudwatch.types.evaluation_periods.EvaluationPeriods"
    ]
    r"""<p>The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an \"M out of N\" alarm, this value is the N.</p>"""
    datapoints_to_alarm: NotRequired[
        "aws_sdk_cloudwatch.types.datapoints_to_alarm.DatapointsToAlarm"
    ]
    r"""<p>The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an \"M out of N\" alarm. In that case, this value is the M. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation\">Evaluating an Alarm</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""
    threshold: NotRequired["aws_sdk_cloudwatch.types.threshold.Threshold"]
    """<p>The value against which the specified statistic is compared.</p> <p>This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.</p>"""
    comparison_operator: NotRequired[
        "aws_sdk_cloudwatch.types.comparison_operator.ComparisonOperator"
    ]
    """<p> The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.</p> <p>The values <code>LessThanLowerOrGreaterThanUpperThreshold</code>, <code>LessThanLowerThreshold</code>, and <code>GreaterThanUpperThreshold</code> are used only for alarms based on anomaly detection models.</p>"""
    treat_missing_data: NotRequired[
        "aws_sdk_cloudwatch.types.treat_missing_data.TreatMissingData"
    ]
    r"""<p> Sets how this alarm is to handle missing data points. If <code>TreatMissingData</code> is omitted, the default behavior of <code>missing</code> is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data\">Configuring How CloudWatch Alarms Treats Missing Data</a>.</p> <p>Valid Values: <code>breaching | notBreaching | ignore | missing</code> </p> <note> <p>Alarms that evaluate metrics in the <code>AWS/DynamoDB</code> namespace always <code>ignore</code> missing data even if you choose a different option for <code>TreatMissingData</code>. When an <code>AWS/DynamoDB</code> metric has missing data, alarms that evaluate that metric remain in their current state.</p> </note> <note> <p>This parameter is not applicable to PromQL alarms.</p> </note>"""
    evaluate_low_sample_count_percentile: NotRequired[
        "aws_sdk_cloudwatch.types.evaluate_low_sample_count_percentile.EvaluateLowSampleCountPercentile"
    ]
    r"""<p> Used only for alarms based on percentiles. If you specify <code>ignore</code>, the alarm state does not change during periods with too few data points to be statistically significant. If you specify <code>evaluate</code> or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples\">Percentile-Based CloudWatch Alarms and Low Data Samples</a>.</p> <p>Valid Values: <code>evaluate | ignore</code> </p>"""
    metrics: NotRequired[
        "aws_sdk_cloudwatch.types.metric_data_queries.MetricDataQueries"
    ]
    r"""<p>An array of <code>MetricDataQuery</code> structures that enable you to create an alarm based on the result of a metric math expression. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code>, a <code>Metrics</code> array, or an <code>EvaluationCriteria</code>.</p> <p>Each item in the <code>Metrics</code> array either retrieves a metric or performs a math expression.</p> <p>One item in the <code>Metrics</code> array is the expression that the alarm watches. You designate this expression by setting <code>ReturnData</code> to true for this object in the array. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataQuery.html\">MetricDataQuery</a>.</p> <p>If you use the <code>Metrics</code> parameter, you cannot include the <code>Namespace</code>, <code>MetricName</code>, <code>Dimensions</code>, <code>Period</code>, <code>Unit</code>, <code>Statistic</code>, or <code>ExtendedStatistic</code> parameters of <code>PutMetricAlarm</code> in the same operation. Instead, you retrieve the metrics you are using in your math expression as part of the <code>Metrics</code> array.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch.types.tag_list.TagList"]
    r"""<p>A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html\">TagResource</a> or <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html\">UntagResource</a>.</p> <p>To use this field to set tags for an alarm when you create it, you must be signed on with both the <code>cloudwatch:PutMetricAlarm</code> and <code>cloudwatch:TagResource</code> permissions.</p>"""
    threshold_metric_id: NotRequired["aws_sdk_cloudwatch.types.metric_id.MetricId"]
    """<p>If this is an alarm based on an anomaly detection model, make this value match the ID of the <code>ANOMALY_DETECTION_BAND</code> function.</p> <p>For an example of how to use this parameter, see the <b>Anomaly Detection Model Alarm</b> example on this page.</p> <p>If your alarm uses this parameter, it cannot have Auto Scaling actions.</p>"""
    evaluation_criteria: NotRequired[
        "aws_sdk_cloudwatch.types.evaluation_criteria.EvaluationCriteria"
    ]
    """<p>The evaluation criteria for the alarm. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code>, a <code>Metrics</code> array, or an <code>EvaluationCriteria</code>.</p> <p>If you use the <code>EvaluationCriteria</code> parameter, you cannot include the <code>Namespace</code>, <code>MetricName</code>, <code>Dimensions</code>, <code>Period</code>, <code>Unit</code>, <code>Statistic</code>, <code>ExtendedStatistic</code>, <code>Metrics</code>, <code>Threshold</code>, <code>ComparisonOperator</code>, <code>ThresholdMetricId</code>, <code>EvaluationPeriods</code>, or <code>DatapointsToAlarm</code> parameters of <code>PutMetricAlarm</code> in the same operation. Instead, all evaluation parameters are defined within this structure.</p> <p>For an example of how to use this parameter, see the <b>PromQL alarm</b> example on this page.</p>"""
    evaluation_interval: NotRequired[
        "aws_sdk_cloudwatch.types.evaluation_interval.EvaluationInterval"
    ]
    """<p>The frequency, in seconds, at which the alarm is evaluated. Valid values are 10, 20, 30, and any multiple of 60.</p> <p>This parameter is required for alarms that use <code>EvaluationCriteria</code>, and cannot be specified for alarms configured with <code>MetricName</code> or <code>Metrics</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMetricAlarmInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_description" in value:
        out["AlarmDescription"] = value["alarm_description"]
    if "actions_enabled" in value:
        out["ActionsEnabled"] = value["actions_enabled"]
    if "ok_actions" in value:
        import aws_sdk_cloudwatch.types.resource_list

        out["OKActions"] = (
            aws_sdk_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["ok_actions"]
            )
        )
    if "alarm_actions" in value:
        import aws_sdk_cloudwatch.types.resource_list

        out["AlarmActions"] = (
            aws_sdk_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["alarm_actions"]
            )
        )
    if "insufficient_data_actions" in value:
        import aws_sdk_cloudwatch.types.resource_list

        out["InsufficientDataActions"] = (
            aws_sdk_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["insufficient_data_actions"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "statistic" in value:
        import aws_sdk_cloudwatch.types.statistic

        out["Statistic"] = aws_sdk_cloudwatch.types.statistic.serialize_aws_json_1_0(
            value["statistic"]
        )
    if "extended_statistic" in value:
        out["ExtendedStatistic"] = value["extended_statistic"]
    if "dimensions" in value:
        import aws_sdk_cloudwatch.types.dimensions

        out["Dimensions"] = aws_sdk_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "unit" in value:
        import aws_sdk_cloudwatch.types.standard_unit

        out["Unit"] = aws_sdk_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    if "evaluation_periods" in value:
        out["EvaluationPeriods"] = value["evaluation_periods"]
    if "datapoints_to_alarm" in value:
        out["DatapointsToAlarm"] = value["datapoints_to_alarm"]
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "comparison_operator" in value:
        import aws_sdk_cloudwatch.types.comparison_operator

        out["ComparisonOperator"] = (
            aws_sdk_cloudwatch.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison_operator"]
            )
        )
    if "treat_missing_data" in value:
        out["TreatMissingData"] = value["treat_missing_data"]
    if "evaluate_low_sample_count_percentile" in value:
        out["EvaluateLowSampleCountPercentile"] = value[
            "evaluate_low_sample_count_percentile"
        ]
    if "metrics" in value:
        import aws_sdk_cloudwatch.types.metric_data_queries

        out["Metrics"] = (
            aws_sdk_cloudwatch.types.metric_data_queries.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        out["Tags"] = aws_sdk_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "threshold_metric_id" in value:
        out["ThresholdMetricId"] = value["threshold_metric_id"]
    if "evaluation_criteria" in value:
        import aws_sdk_cloudwatch.types.evaluation_criteria

        out["EvaluationCriteria"] = (
            aws_sdk_cloudwatch.types.evaluation_criteria.serialize_aws_json_1_0(
                value["evaluation_criteria"]
            )
        )
    if "evaluation_interval" in value:
        out["EvaluationInterval"] = value["evaluation_interval"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMetricAlarmInput:
    out: PutMetricAlarmInput = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    if "AlarmDescription" in data:
        out["alarm_description"] = data["AlarmDescription"]
    if "ActionsEnabled" in data:
        out["actions_enabled"] = data["ActionsEnabled"]
    if "OKActions" in data:
        import aws_sdk_cloudwatch.types.resource_list

        out["ok_actions"] = (
            aws_sdk_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["OKActions"]
            )
        )
    if "AlarmActions" in data:
        import aws_sdk_cloudwatch.types.resource_list

        out["alarm_actions"] = (
            aws_sdk_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["AlarmActions"]
            )
        )
    if "InsufficientDataActions" in data:
        import aws_sdk_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            aws_sdk_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["InsufficientDataActions"]
            )
        )
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Statistic" in data:
        import aws_sdk_cloudwatch.types.statistic

        out["statistic"] = aws_sdk_cloudwatch.types.statistic.deserialize_aws_json_1_0(
            data["Statistic"]
        )
    if "ExtendedStatistic" in data:
        out["extended_statistic"] = data["ExtendedStatistic"]
    if "Dimensions" in data:
        import aws_sdk_cloudwatch.types.dimensions

        out["dimensions"] = (
            aws_sdk_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    if "Period" in data:
        out["period"] = data["Period"]
    if "Unit" in data:
        import aws_sdk_cloudwatch.types.standard_unit

        out["unit"] = aws_sdk_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    if "EvaluationPeriods" in data:
        out["evaluation_periods"] = data["EvaluationPeriods"]
    if "DatapointsToAlarm" in data:
        out["datapoints_to_alarm"] = data["DatapointsToAlarm"]
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "ComparisonOperator" in data:
        import aws_sdk_cloudwatch.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_cloudwatch.types.comparison_operator.deserialize_aws_json_1_0(
                data["ComparisonOperator"]
            )
        )
    if "TreatMissingData" in data:
        out["treat_missing_data"] = data["TreatMissingData"]
    if "EvaluateLowSampleCountPercentile" in data:
        out["evaluate_low_sample_count_percentile"] = data[
            "EvaluateLowSampleCountPercentile"
        ]
    if "Metrics" in data:
        import aws_sdk_cloudwatch.types.metric_data_queries

        out["metrics"] = (
            aws_sdk_cloudwatch.types.metric_data_queries.deserialize_aws_json_1_0(
                data["Metrics"]
            )
        )
    if "Tags" in data:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "ThresholdMetricId" in data:
        out["threshold_metric_id"] = data["ThresholdMetricId"]
    if "EvaluationCriteria" in data:
        import aws_sdk_cloudwatch.types.evaluation_criteria

        out["evaluation_criteria"] = (
            aws_sdk_cloudwatch.types.evaluation_criteria.deserialize_aws_json_1_0(
                data["EvaluationCriteria"]
            )
        )
    if "EvaluationInterval" in data:
        out["evaluation_interval"] = data["EvaluationInterval"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutMetricAlarmInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_name" in value:
        pairs.append((f"{prefix}.AlarmName", str(value["alarm_name"])))
    if "alarm_description" in value:
        pairs.append((f"{prefix}.AlarmDescription", str(value["alarm_description"])))
    if "actions_enabled" in value:
        pairs.append(
            (
                f"{prefix}.ActionsEnabled",
                "true" if value["actions_enabled"] else "false",
            )
        )
    if "ok_actions" in value:
        import aws_sdk_cloudwatch.types.resource_list

        aws_sdk_cloudwatch.types.resource_list.serialize_query(
            value["ok_actions"], pairs, f"{prefix}.OKActions"
        )
    if "alarm_actions" in value:
        import aws_sdk_cloudwatch.types.resource_list

        aws_sdk_cloudwatch.types.resource_list.serialize_query(
            value["alarm_actions"], pairs, f"{prefix}.AlarmActions"
        )
    if "insufficient_data_actions" in value:
        import aws_sdk_cloudwatch.types.resource_list

        aws_sdk_cloudwatch.types.resource_list.serialize_query(
            value["insufficient_data_actions"],
            pairs,
            f"{prefix}.InsufficientDataActions",
        )
    if "metric_name" in value:
        pairs.append((f"{prefix}.MetricName", str(value["metric_name"])))
    if "namespace" in value:
        pairs.append((f"{prefix}.Namespace", str(value["namespace"])))
    if "statistic" in value:
        import aws_sdk_cloudwatch.types.statistic

        aws_sdk_cloudwatch.types.statistic.serialize_query(
            value["statistic"], pairs, f"{prefix}.Statistic"
        )
    if "extended_statistic" in value:
        pairs.append((f"{prefix}.ExtendedStatistic", str(value["extended_statistic"])))
    if "dimensions" in value:
        import aws_sdk_cloudwatch.types.dimensions

        aws_sdk_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{prefix}.Dimensions"
        )
    if "period" in value:
        pairs.append((f"{prefix}.Period", str(value["period"])))
    if "unit" in value:
        import aws_sdk_cloudwatch.types.standard_unit

        aws_sdk_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{prefix}.Unit"
        )
    if "evaluation_periods" in value:
        pairs.append((f"{prefix}.EvaluationPeriods", str(value["evaluation_periods"])))
    if "datapoints_to_alarm" in value:
        pairs.append((f"{prefix}.DatapointsToAlarm", str(value["datapoints_to_alarm"])))
    if "threshold" in value:
        pairs.append((f"{prefix}.Threshold", str(value["threshold"])))
    if "comparison_operator" in value:
        import aws_sdk_cloudwatch.types.comparison_operator

        aws_sdk_cloudwatch.types.comparison_operator.serialize_query(
            value["comparison_operator"], pairs, f"{prefix}.ComparisonOperator"
        )
    if "treat_missing_data" in value:
        pairs.append((f"{prefix}.TreatMissingData", str(value["treat_missing_data"])))
    if "evaluate_low_sample_count_percentile" in value:
        pairs.append(
            (
                f"{prefix}.EvaluateLowSampleCountPercentile",
                str(value["evaluate_low_sample_count_percentile"]),
            )
        )
    if "metrics" in value:
        import aws_sdk_cloudwatch.types.metric_data_queries

        aws_sdk_cloudwatch.types.metric_data_queries.serialize_query(
            value["metrics"], pairs, f"{prefix}.Metrics"
        )
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        aws_sdk_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "threshold_metric_id" in value:
        pairs.append((f"{prefix}.ThresholdMetricId", str(value["threshold_metric_id"])))
    if "evaluation_criteria" in value:
        import aws_sdk_cloudwatch.types.evaluation_criteria

        aws_sdk_cloudwatch.types.evaluation_criteria.serialize_query(
            value["evaluation_criteria"], pairs, f"{prefix}.EvaluationCriteria"
        )
    if "evaluation_interval" in value:
        pairs.append(
            (f"{prefix}.EvaluationInterval", str(value["evaluation_interval"]))
        )


def deserialize_query(el: Element) -> PutMetricAlarmInput:
    out: PutMetricAlarmInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_description = el.find("AlarmDescription")
    if child_alarm_description is not None:
        out["alarm_description"] = str(child_alarm_description.text or "")
    child_actions_enabled = el.find("ActionsEnabled")
    if child_actions_enabled is not None:
        out["actions_enabled"] = (child_actions_enabled.text or "").lower() == "true"
    child_ok_actions = el.find("OKActions")
    if child_ok_actions is not None:
        import aws_sdk_cloudwatch.types.resource_list

        out["ok_actions"] = aws_sdk_cloudwatch.types.resource_list.deserialize_query(
            child_ok_actions
        )
    child_alarm_actions = el.find("AlarmActions")
    if child_alarm_actions is not None:
        import aws_sdk_cloudwatch.types.resource_list

        out["alarm_actions"] = aws_sdk_cloudwatch.types.resource_list.deserialize_query(
            child_alarm_actions
        )
    child_insufficient_data_actions = el.find("InsufficientDataActions")
    if child_insufficient_data_actions is not None:
        import aws_sdk_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            aws_sdk_cloudwatch.types.resource_list.deserialize_query(
                child_insufficient_data_actions
            )
        )
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import aws_sdk_cloudwatch.types.statistic

        out["statistic"] = aws_sdk_cloudwatch.types.statistic.deserialize_query(
            child_statistic
        )
    child_extended_statistic = el.find("ExtendedStatistic")
    if child_extended_statistic is not None:
        out["extended_statistic"] = str(child_extended_statistic.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import aws_sdk_cloudwatch.types.dimensions

        out["dimensions"] = aws_sdk_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        import aws_sdk_cloudwatch.types.standard_unit

        out["unit"] = aws_sdk_cloudwatch.types.standard_unit.deserialize_query(
            child_unit
        )
    child_evaluation_periods = el.find("EvaluationPeriods")
    if child_evaluation_periods is not None:
        out["evaluation_periods"] = int(child_evaluation_periods.text or "")
    child_datapoints_to_alarm = el.find("DatapointsToAlarm")
    if child_datapoints_to_alarm is not None:
        out["datapoints_to_alarm"] = int(child_datapoints_to_alarm.text or "")
    child_threshold = el.find("Threshold")
    if child_threshold is not None:
        out["threshold"] = float(child_threshold.text or "")
    child_comparison_operator = el.find("ComparisonOperator")
    if child_comparison_operator is not None:
        import aws_sdk_cloudwatch.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_cloudwatch.types.comparison_operator.deserialize_query(
                child_comparison_operator
            )
        )
    child_treat_missing_data = el.find("TreatMissingData")
    if child_treat_missing_data is not None:
        out["treat_missing_data"] = str(child_treat_missing_data.text or "")
    child_evaluate_low_sample_count_percentile = el.find(
        "EvaluateLowSampleCountPercentile"
    )
    if child_evaluate_low_sample_count_percentile is not None:
        out["evaluate_low_sample_count_percentile"] = str(
            child_evaluate_low_sample_count_percentile.text or ""
        )
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import aws_sdk_cloudwatch.types.metric_data_queries

        out["metrics"] = aws_sdk_cloudwatch.types.metric_data_queries.deserialize_query(
            child_metrics
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_query(child_tags)
    child_threshold_metric_id = el.find("ThresholdMetricId")
    if child_threshold_metric_id is not None:
        out["threshold_metric_id"] = str(child_threshold_metric_id.text or "")
    child_evaluation_criteria = el.find("EvaluationCriteria")
    if child_evaluation_criteria is not None:
        import aws_sdk_cloudwatch.types.evaluation_criteria

        out["evaluation_criteria"] = (
            aws_sdk_cloudwatch.types.evaluation_criteria.deserialize_query(
                child_evaluation_criteria
            )
        )
    child_evaluation_interval = el.find("EvaluationInterval")
    if child_evaluation_interval is not None:
        out["evaluation_interval"] = int(child_evaluation_interval.text or "")
    return out
