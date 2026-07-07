"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyMonitor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.monitor_dimension
    import aws_sdk_cost_explorer.types.monitor_type
    import aws_sdk_cost_explorer.types.non_negative_integer
    import aws_sdk_cost_explorer.types.year_month_day


class AnomalyMonitor(TypedDict, closed=True):
    monitor_arn: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Resource Name (ARN) value. </p>"""
    monitor_name: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The name of the monitor. </p>"""
    creation_date: NotRequired[
        "aws_sdk_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The date when the monitor was created. </p>"""
    last_updated_date: NotRequired[
        "aws_sdk_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The date when the monitor was last updated. </p>"""
    last_evaluated_date: NotRequired[
        "aws_sdk_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The date when the monitor last evaluated for anomalies. </p>"""
    monitor_type: "aws_sdk_cost_explorer.types.monitor_type.MonitorType"
    r"""<p>The type of the monitor. </p> <p>Set this to <code>DIMENSIONAL</code> for an Amazon Web Services managed monitor. Amazon Web Services managed monitors automatically track up to the top 5,000 values by cost within a dimension of your choosing. Each dimension value is evaluated independently. If you start incurring cost in a new value of your chosen dimension, it will automatically be analyzed by an Amazon Web Services managed monitor.</p> <p>Set this to <code>CUSTOM</code> for a customer managed monitor. Customer managed monitors let you select specific dimension values that get monitored in aggregate. </p> <p>For more information about monitor types, see <a href=\"https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html#monitor-type-def\">Monitor types</a> in the <i>Billing and Cost Management User Guide</i>.</p>"""
    monitor_dimension: NotRequired[
        "aws_sdk_cost_explorer.types.monitor_dimension.MonitorDimension"
    ]
    """<p>For customer managed monitors, do not specify this field.</p> <p>For Amazon Web Services managed monitors, this field controls which cost dimension is automatically analyzed by the monitor. For <code>TAG</code> and <code>COST_CATEGORY </code> dimensions, you must also specify MonitorSpecification to configure the specific tag or cost category key to analyze.</p>"""
    monitor_specification: NotRequired[
        "aws_sdk_cost_explorer.types.expression.Expression"
    ]
    r"""<p>An <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html\">Expression</a> object used to control what costs the monitor analyzes for anomalies.</p> <p>For Amazon Web Services managed monitors:</p> <ul> <li> <p>If MonitorDimension is <code>SERVICE</code> or <code>LINKED_ACCOUNT</code>, do not specify this field</p> </li> <li> <p>If MonitorDimension is <code>TAG</code>, set this field to <code>{ \"Tags\": { \"Key\": \"your tag key\" } }</code> </p> </li> <li> <p>If MonitorDimension is <code>COST_CATEGORY</code>, set this field to <code>{ \"CostCategories\": { \"Key\": \"your cost category key\" } }</code> </p> </li> </ul> <p>For customer managed monitors:</p> <ul> <li> <p>To track linked accounts, set this field to <code>{ \"Dimensions\": { \"Key\": \"LINKED_ACCOUNT\", \"Values\": [ \"your list of up to 10 account IDs\" ] } } </code> </p> </li> <li> <p>To track cost allocation tags, set this field to <code>{ \"Tags\": { \"Key\": \"your tag key\", \"Values\": [ \"your list of up to 10 tag values\" ] } } </code> </p> </li> <li> <p>To track cost categories, set this field to<code>{ \"CostCategories\": { \"Key\": \"your cost category key\", \"Values\": [ \"your cost category value\" ] } } </code> </p> </li> </ul>"""
    dimensional_value_count: (
        "aws_sdk_cost_explorer.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The value for evaluated dimensions. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyMonitor) -> dict:
    out: dict = {}
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    out["MonitorName"] = value["monitor_name"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "last_updated_date" in value:
        out["LastUpdatedDate"] = value["last_updated_date"]
    if "last_evaluated_date" in value:
        out["LastEvaluatedDate"] = value["last_evaluated_date"]
    import aws_sdk_cost_explorer.types.monitor_type

    out["MonitorType"] = (
        aws_sdk_cost_explorer.types.monitor_type.serialize_aws_json_1_1(
            value["monitor_type"]
        )
    )
    if "monitor_dimension" in value:
        import aws_sdk_cost_explorer.types.monitor_dimension

        out["MonitorDimension"] = (
            aws_sdk_cost_explorer.types.monitor_dimension.serialize_aws_json_1_1(
                value["monitor_dimension"]
            )
        )
    if "monitor_specification" in value:
        import aws_sdk_cost_explorer.types.expression

        out["MonitorSpecification"] = (
            aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["monitor_specification"]
            )
        )
    out["DimensionalValueCount"] = value.get("dimensional_value_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalyMonitor:
    out: AnomalyMonitor = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    else:
        raise DeserializationError("AnomalyMonitor.monitor_name required")
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "LastUpdatedDate" in data:
        out["last_updated_date"] = data["LastUpdatedDate"]
    if "LastEvaluatedDate" in data:
        out["last_evaluated_date"] = data["LastEvaluatedDate"]
    if "MonitorType" in data:
        import aws_sdk_cost_explorer.types.monitor_type

        out["monitor_type"] = (
            aws_sdk_cost_explorer.types.monitor_type.deserialize_aws_json_1_1(
                data["MonitorType"]
            )
        )
    else:
        raise DeserializationError("AnomalyMonitor.monitor_type required")
    if "MonitorDimension" in data:
        import aws_sdk_cost_explorer.types.monitor_dimension

        out["monitor_dimension"] = (
            aws_sdk_cost_explorer.types.monitor_dimension.deserialize_aws_json_1_1(
                data["MonitorDimension"]
            )
        )
    if "MonitorSpecification" in data:
        import aws_sdk_cost_explorer.types.expression

        out["monitor_specification"] = (
            aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["MonitorSpecification"]
            )
        )
    if "DimensionalValueCount" in data:
        out["dimensional_value_count"] = data["DimensionalValueCount"]
    else:
        out["dimensional_value_count"] = 0
    return out
