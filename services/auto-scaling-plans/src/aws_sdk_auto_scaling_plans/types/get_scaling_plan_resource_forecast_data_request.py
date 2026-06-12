"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#GetScalingPlanResourceForecastDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.forecast_data_type
    import aws_sdk_auto_scaling_plans.types.scalable_dimension
    import aws_sdk_auto_scaling_plans.types.scaling_plan_name
    import aws_sdk_auto_scaling_plans.types.scaling_plan_version
    import aws_sdk_auto_scaling_plans.types.service_namespace
    import aws_sdk_auto_scaling_plans.types.timestamp_type
    import aws_sdk_auto_scaling_plans.types.xml_string


class GetScalingPlanResourceForecastDataRequest(TypedDict):
    scaling_plan_name: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    )
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>"""
    service_namespace: (
        "aws_sdk_auto_scaling_plans.types.service_namespace.ServiceNamespace"
    )
    """<p>The namespace of the AWS service. The only valid value is <code>autoscaling</code>. </p>"""
    resource_id: "aws_sdk_auto_scaling_plans.types.xml_string.XmlString"
    """<p>The ID of the resource. This string consists of a prefix (<code>autoScalingGroup</code>) followed by the name of a specified Auto Scaling group (<code>my-asg</code>). Example: <code>autoScalingGroup/my-asg</code>. </p>"""
    scalable_dimension: (
        "aws_sdk_auto_scaling_plans.types.scalable_dimension.ScalableDimension"
    )
    """<p>The scalable dimension for the resource. The only valid value is <code>autoscaling:autoScalingGroup:DesiredCapacity</code>. </p>"""
    forecast_data_type: (
        "aws_sdk_auto_scaling_plans.types.forecast_data_type.ForecastDataType"
    )
    """<p>The type of forecast data to get.</p> <ul> <li> <p> <code>LoadForecast</code>: The load metric forecast. </p> </li> <li> <p> <code>CapacityForecast</code>: The capacity forecast. </p> </li> <li> <p> <code>ScheduledActionMinCapacity</code>: The minimum capacity for each scheduled scaling action. This data is calculated as the larger of two values: the capacity forecast or the minimum capacity in the scaling instruction.</p> </li> <li> <p> <code>ScheduledActionMaxCapacity</code>: The maximum capacity for each scheduled scaling action. The calculation used is determined by the predictive scaling maximum capacity behavior setting in the scaling instruction.</p> </li> </ul>"""
    start_time: "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType"
    """<p>The inclusive start time of the time range for the forecast data to get. The date and time can be at most 56 days before the current date and time. </p>"""
    end_time: "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType"
    """<p>The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is seven days. </p> <p>Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. AWS Auto Scaling only issues forecasts for periods of two days in advance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScalingPlanResourceForecastDataRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    import aws_sdk_auto_scaling_plans.types.service_namespace

    out["ServiceNamespace"] = (
        aws_sdk_auto_scaling_plans.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_auto_scaling_plans.types.scalable_dimension

    out["ScalableDimension"] = (
        aws_sdk_auto_scaling_plans.types.scalable_dimension.serialize_aws_json_1_1(
            value["scalable_dimension"]
        )
    )
    import aws_sdk_auto_scaling_plans.types.forecast_data_type

    out["ForecastDataType"] = (
        aws_sdk_auto_scaling_plans.types.forecast_data_type.serialize_aws_json_1_1(
            value["forecast_data_type"]
        )
    )
    import aws_sdk_auto_scaling_plans.types.timestamp_type

    out["StartTime"] = (
        aws_sdk_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
            value["start_time"]
        )
    )
    import aws_sdk_auto_scaling_plans.types.timestamp_type

    out["EndTime"] = (
        aws_sdk_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
            value["end_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScalingPlanResourceForecastDataRequest:
    out: GetScalingPlanResourceForecastDataRequest = {}  # type: ignore[typeddict-item]
    if "ScalingPlanName" in data:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.scaling_plan_name required"
        )
    if "ScalingPlanVersion" in data:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.scaling_plan_version required"
        )
    if "ServiceNamespace" in data:
        import aws_sdk_auto_scaling_plans.types.service_namespace

        out["service_namespace"] = (
            aws_sdk_auto_scaling_plans.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.service_namespace required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.resource_id required"
        )
    if "ScalableDimension" in data:
        import aws_sdk_auto_scaling_plans.types.scalable_dimension

        out["scalable_dimension"] = (
            aws_sdk_auto_scaling_plans.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.scalable_dimension required"
        )
    if "ForecastDataType" in data:
        import aws_sdk_auto_scaling_plans.types.forecast_data_type

        out["forecast_data_type"] = (
            aws_sdk_auto_scaling_plans.types.forecast_data_type.deserialize_aws_json_1_1(
                data["ForecastDataType"]
            )
        )
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.forecast_data_type required"
        )
    if "StartTime" in data:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["start_time"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.start_time required"
        )
    if "EndTime" in data:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["end_time"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetScalingPlanResourceForecastDataRequest.end_time required"
        )
    return out
