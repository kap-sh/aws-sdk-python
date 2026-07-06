"""Generated from Smithy shape ``com.amazonaws.athena#EngineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.classification_list
    import aws_sdk_athena.types.coordinator_dpu_size
    import aws_sdk_athena.types.default_executor_dpu_size
    import aws_sdk_athena.types.max_concurrent_dpus
    import aws_sdk_athena.types.parameters_map


class EngineConfiguration(TypedDict, closed=True):
    coordinator_dpu_size: NotRequired[
        "aws_sdk_athena.types.coordinator_dpu_size.CoordinatorDpuSize"
    ]
    """<p>The number of DPUs to use for the coordinator. A coordinator is a special executor that orchestrates processing work and manages other executors in a notebook session. The default is 1.</p>"""
    max_concurrent_dpus: "aws_sdk_athena.types.max_concurrent_dpus.MaxConcurrentDpus"
    """<p>The maximum number of DPUs that can run concurrently.</p>"""
    default_executor_dpu_size: NotRequired[
        "aws_sdk_athena.types.default_executor_dpu_size.DefaultExecutorDpuSize"
    ]
    """<p>The default number of DPUs to use for executors. An executor is the smallest unit of compute that a notebook session can request from Athena. The default is 1.</p>"""
    additional_configs: NotRequired["aws_sdk_athena.types.parameters_map.ParametersMap"]
    """<p>Contains additional notebook engine <code>MAP<string, string></code> parameter mappings in the form of key-value pairs. To specify an Athena notebook that the Jupyter server will download and serve, specify a value for the <a>StartSessionRequest$NotebookVersion</a> field, and then add a key named <code>NotebookId</code> to <code>AdditionalConfigs</code> that has the value of the Athena notebook ID.</p>"""
    spark_properties: NotRequired["aws_sdk_athena.types.parameters_map.ParametersMap"]
    """<p>Specifies custom jar files and Spark properties for use cases like cluster encryption, table formats, and general Spark tuning.</p>"""
    classifications: NotRequired[
        "aws_sdk_athena.types.classification_list.ClassificationList"
    ]
    """<p>The configuration classifications that can be specified for the engine.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineConfiguration) -> dict:
    out: dict = {}
    if "coordinator_dpu_size" in value:
        out["CoordinatorDpuSize"] = value["coordinator_dpu_size"]
    out["MaxConcurrentDpus"] = value.get("max_concurrent_dpus", 20)
    if "default_executor_dpu_size" in value:
        out["DefaultExecutorDpuSize"] = value["default_executor_dpu_size"]
    if "additional_configs" in value:
        import aws_sdk_athena.types.parameters_map

        out["AdditionalConfigs"] = (
            aws_sdk_athena.types.parameters_map.serialize_aws_json_1_1(
                value["additional_configs"]
            )
        )
    if "spark_properties" in value:
        import aws_sdk_athena.types.parameters_map

        out["SparkProperties"] = (
            aws_sdk_athena.types.parameters_map.serialize_aws_json_1_1(
                value["spark_properties"]
            )
        )
    if "classifications" in value:
        import aws_sdk_athena.types.classification_list

        out["Classifications"] = (
            aws_sdk_athena.types.classification_list.serialize_aws_json_1_1(
                value["classifications"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EngineConfiguration:
    out: EngineConfiguration = {}  # type: ignore[typeddict-item]
    if "CoordinatorDpuSize" in data:
        out["coordinator_dpu_size"] = data["CoordinatorDpuSize"]
    if "MaxConcurrentDpus" in data:
        out["max_concurrent_dpus"] = data["MaxConcurrentDpus"]
    else:
        out["max_concurrent_dpus"] = 20
    if "DefaultExecutorDpuSize" in data:
        out["default_executor_dpu_size"] = data["DefaultExecutorDpuSize"]
    if "AdditionalConfigs" in data:
        import aws_sdk_athena.types.parameters_map

        out["additional_configs"] = (
            aws_sdk_athena.types.parameters_map.deserialize_aws_json_1_1(
                data["AdditionalConfigs"]
            )
        )
    if "SparkProperties" in data:
        import aws_sdk_athena.types.parameters_map

        out["spark_properties"] = (
            aws_sdk_athena.types.parameters_map.deserialize_aws_json_1_1(
                data["SparkProperties"]
            )
        )
    if "Classifications" in data:
        import aws_sdk_athena.types.classification_list

        out["classifications"] = (
            aws_sdk_athena.types.classification_list.deserialize_aws_json_1_1(
                data["Classifications"]
            )
        )
    return out
