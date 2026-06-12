"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ParallelismConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object
    import aws_sdk_kinesis_analytics_v2.types.configuration_type
    import aws_sdk_kinesis_analytics_v2.types.parallelism
    import aws_sdk_kinesis_analytics_v2.types.parallelism_per_kpu


class ParallelismConfigurationUpdate(TypedDict):
    configuration_type_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    ]
    """<p>Describes updates to whether the application uses the default parallelism for the Managed Service for Apache Flink service, or if a custom parallelism is used. You must set this property to <code>CUSTOM</code> in order to change your application's <code>AutoScalingEnabled</code>, <code>Parallelism</code>, or <code>ParallelismPerKPU</code> properties.</p>"""
    parallelism_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.parallelism.Parallelism"
    ]
    """<p>Describes updates to the initial number of parallel tasks an application can perform. If <code>AutoScalingEnabled</code> is set to True, then Managed Service for Apache Flink can increase the <code>CurrentParallelism</code> value in response to application load. The service can increase <code>CurrentParallelism</code> up to the maximum parallelism, which is <code>ParalellismPerKPU</code> times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service will reduce <code>CurrentParallelism</code> down to the <code>Parallelism</code> setting.</p>"""
    parallelism_per_kpu_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.parallelism_per_kpu.ParallelismPerKPU"
    ]
    """<p>Describes updates to the number of parallel tasks an application can perform per Kinesis Processing Unit (KPU) used by the application.</p>"""
    auto_scaling_enabled_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>Describes updates to whether the Managed Service for Apache Flink service can increase the parallelism of a Managed Service for Apache Flink application in response to increased throughput.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelismConfigurationUpdate) -> dict:
    out: dict = {}
    if "configuration_type_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["ConfigurationTypeUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
                value["configuration_type_update"]
            )
        )
    if "parallelism_update" in value:
        out["ParallelismUpdate"] = value["parallelism_update"]
    if "parallelism_per_kpu_update" in value:
        out["ParallelismPerKPUUpdate"] = value["parallelism_per_kpu_update"]
    if "auto_scaling_enabled_update" in value:
        out["AutoScalingEnabledUpdate"] = value["auto_scaling_enabled_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelismConfigurationUpdate:
    out: ParallelismConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "ConfigurationTypeUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["configuration_type_update"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationTypeUpdate"]
            )
        )
    if "ParallelismUpdate" in data:
        out["parallelism_update"] = data["ParallelismUpdate"]
    if "ParallelismPerKPUUpdate" in data:
        out["parallelism_per_kpu_update"] = data["ParallelismPerKPUUpdate"]
    if "AutoScalingEnabledUpdate" in data:
        out["auto_scaling_enabled_update"] = data["AutoScalingEnabledUpdate"]
    return out
