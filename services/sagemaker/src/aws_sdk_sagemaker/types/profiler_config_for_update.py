"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilerConfigForUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.disable_profiler
    import aws_sdk_sagemaker.types.profiling_interval_in_milliseconds
    import aws_sdk_sagemaker.types.profiling_parameters
    import aws_sdk_sagemaker.types.s3_uri


class ProfilerConfigForUpdate(TypedDict):
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>Path to Amazon S3 storage location for system and framework metrics.</p>"""
    profiling_interval_in_milliseconds: NotRequired[
        "aws_sdk_sagemaker.types.profiling_interval_in_milliseconds.ProfilingIntervalInMilliseconds"
    ]
    """<p>A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.</p>"""
    profiling_parameters: NotRequired[
        "aws_sdk_sagemaker.types.profiling_parameters.ProfilingParameters"
    ]
    """<p>Configuration information for capturing framework metrics. Available key strings for different profiling options are <code>DetailedProfilingConfig</code>, <code>PythonProfilingConfig</code>, and <code>DataLoaderProfilingConfig</code>. The following codes are configuration structures for the <code>ProfilingParameters</code> parameter. To learn more about how to configure the <code>ProfilingParameters</code> parameter, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html\">Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job</a>. </p>"""
    disable_profiler: NotRequired[
        "aws_sdk_sagemaker.types.disable_profiler.DisableProfiler"
    ]
    """<p>To turn off Amazon SageMaker Debugger monitoring and profiling while a training job is in progress, set to <code>True</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerConfigForUpdate) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "profiling_interval_in_milliseconds" in value:
        out["ProfilingIntervalInMilliseconds"] = value[
            "profiling_interval_in_milliseconds"
        ]
    if "profiling_parameters" in value:
        import aws_sdk_sagemaker.types.profiling_parameters

        out["ProfilingParameters"] = (
            aws_sdk_sagemaker.types.profiling_parameters.serialize_aws_json_1_1(
                value["profiling_parameters"]
            )
        )
    if "disable_profiler" in value:
        out["DisableProfiler"] = value["disable_profiler"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProfilerConfigForUpdate:
    out: ProfilerConfigForUpdate = {}  # type: ignore[typeddict-item]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    if "ProfilingIntervalInMilliseconds" in data:
        out["profiling_interval_in_milliseconds"] = data[
            "ProfilingIntervalInMilliseconds"
        ]
    if "ProfilingParameters" in data:
        import aws_sdk_sagemaker.types.profiling_parameters

        out["profiling_parameters"] = (
            aws_sdk_sagemaker.types.profiling_parameters.deserialize_aws_json_1_1(
                data["ProfilingParameters"]
            )
        )
    if "DisableProfiler" in data:
        out["disable_profiler"] = data["DisableProfiler"]
    return out
