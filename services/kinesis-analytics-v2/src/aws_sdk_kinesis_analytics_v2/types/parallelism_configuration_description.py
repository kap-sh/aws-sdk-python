"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ParallelismConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object
    import aws_sdk_kinesis_analytics_v2.types.configuration_type
    import aws_sdk_kinesis_analytics_v2.types.parallelism
    import aws_sdk_kinesis_analytics_v2.types.parallelism_per_kpu


class ParallelismConfigurationDescription(TypedDict, closed=True):
    configuration_type: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    ]
    """<p>Describes whether the application uses the default parallelism for the Managed Service for Apache Flink service. </p>"""
    parallelism: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.parallelism.Parallelism"
    ]
    """<p>Describes the initial number of parallel tasks that a Managed Service for Apache Flink application can perform. If <code>AutoScalingEnabled</code> is set to True, then Managed Service for Apache Flink can increase the <code>CurrentParallelism</code> value in response to application load. The service can increase <code>CurrentParallelism</code> up to the maximum parallelism, which is <code>ParalellismPerKPU</code> times the maximum KPUs for the application. The maximum KPUs for an application is 64 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the <code>CurrentParallelism</code> value down to the <code>Parallelism</code> setting.</p>"""
    parallelism_per_kpu: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.parallelism_per_kpu.ParallelismPerKPU"
    ]
    """<p>Describes the number of parallel tasks that a Managed Service for Apache Flink application can perform per Kinesis Processing Unit (KPU) used by the application.</p>"""
    current_parallelism: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.parallelism.Parallelism"
    ]
    """<p>Describes the current number of parallel tasks that a Managed Service for Apache Flink application can perform. If <code>AutoScalingEnabled</code> is set to True, Managed Service for Apache Flink can increase this value in response to application load. The service can increase this value up to the maximum parallelism, which is <code>ParalellismPerKPU</code> times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the <code>CurrentParallelism</code> value down to the <code>Parallelism</code> setting.</p>"""
    auto_scaling_enabled: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>Describes whether the Managed Service for Apache Flink service can increase the parallelism of the application in response to increased throughput.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelismConfigurationDescription) -> dict:
    out: dict = {}
    if "configuration_type" in value:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["ConfigurationType"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
                value["configuration_type"]
            )
        )
    if "parallelism" in value:
        out["Parallelism"] = value["parallelism"]
    if "parallelism_per_kpu" in value:
        out["ParallelismPerKPU"] = value["parallelism_per_kpu"]
    if "current_parallelism" in value:
        out["CurrentParallelism"] = value["current_parallelism"]
    if "auto_scaling_enabled" in value:
        out["AutoScalingEnabled"] = value["auto_scaling_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelismConfigurationDescription:
    out: ParallelismConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "ConfigurationType" in data:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["configuration_type"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationType"]
            )
        )
    if "Parallelism" in data:
        out["parallelism"] = data["Parallelism"]
    if "ParallelismPerKPU" in data:
        out["parallelism_per_kpu"] = data["ParallelismPerKPU"]
    if "CurrentParallelism" in data:
        out["current_parallelism"] = data["CurrentParallelism"]
    if "AutoScalingEnabled" in data:
        out["auto_scaling_enabled"] = data["AutoScalingEnabled"]
    return out
