"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#GetPredictiveScalingForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.policy_name
    import capo_application_auto_scaling.types.resource_id_max_len1600
    import capo_application_auto_scaling.types.scalable_dimension
    import capo_application_auto_scaling.types.service_namespace
    import capo_application_auto_scaling.types.timestamp_type


class GetPredictiveScalingForecastRequest(TypedDict, closed=True):
    service_namespace: (
        "capo_application_auto_scaling.types.service_namespace.ServiceNamespace"
    )
    """<p> The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use <code>custom-resource</code> instead. </p>"""
    resource_id: "capo_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p> The identifier of the resource. </p>"""
    scalable_dimension: (
        "capo_application_auto_scaling.types.scalable_dimension.ScalableDimension"
    )
    """<p> The scalable dimension. </p>"""
    policy_name: "capo_application_auto_scaling.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    start_time: "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    """<p> The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time </p>"""
    end_time: "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    """<p> The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPredictiveScalingForecastRequest) -> dict:
    out: dict = {}
    import capo_application_auto_scaling.types.service_namespace

    out["ServiceNamespace"] = (
        capo_application_auto_scaling.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_application_auto_scaling.types.scalable_dimension

    out["ScalableDimension"] = (
        capo_application_auto_scaling.types.scalable_dimension.serialize_aws_json_1_1(
            value["scalable_dimension"]
        )
    )
    out["PolicyName"] = value["policy_name"]
    import capo_application_auto_scaling.types.timestamp_type

    out["StartTime"] = (
        capo_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
            value["start_time"]
        )
    )
    import capo_application_auto_scaling.types.timestamp_type

    out["EndTime"] = (
        capo_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
            value["end_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPredictiveScalingForecastRequest:
    out: GetPredictiveScalingForecastRequest = {}  # type: ignore[typeddict-item]
    if "ServiceNamespace" in data:
        import capo_application_auto_scaling.types.service_namespace

        out["service_namespace"] = (
            capo_application_auto_scaling.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        raise DeserializationError(
            "GetPredictiveScalingForecastRequest.service_namespace required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "GetPredictiveScalingForecastRequest.resource_id required"
        )
    if "ScalableDimension" in data:
        import capo_application_auto_scaling.types.scalable_dimension

        out["scalable_dimension"] = (
            capo_application_auto_scaling.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    else:
        raise DeserializationError(
            "GetPredictiveScalingForecastRequest.scalable_dimension required"
        )
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError(
            "GetPredictiveScalingForecastRequest.policy_name required"
        )
    if "StartTime" in data:
        import capo_application_auto_scaling.types.timestamp_type

        out["start_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetPredictiveScalingForecastRequest.start_time required"
        )
    if "EndTime" in data:
        import capo_application_auto_scaling.types.timestamp_type

        out["end_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetPredictiveScalingForecastRequest.end_time required"
        )
    return out
