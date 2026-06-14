"""Generated from Smithy shape ``com.amazonaws.datazone#SparkGluePropertiesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glue_connection_names
    import aws_sdk_datazone.types.spark_glue_args


class SparkGluePropertiesInput(TypedDict):
    additional_args: NotRequired["aws_sdk_datazone.types.spark_glue_args.SparkGlueArgs"]
    """<p>The additional args in the Spark Amazon Web Services Glue properties.</p>"""
    glue_connection_name: NotRequired["str"]
    """<p>The Amazon Web Services Glue connection name in the Spark Amazon Web Services Glue properties. Specify either <code>glueConnectionName</code> or <code>glueConnectionNames</code>, but not both.</p>"""
    glue_connection_names: NotRequired[
        "aws_sdk_datazone.types.glue_connection_names.GlueConnectionNames"
    ]
    """<p>The Amazon Web Services Glue connection names in the Spark Amazon Web Services Glue properties. Specify either <code>glueConnectionName</code> or <code>glueConnectionNames</code>, but not both.</p>"""
    glue_version: NotRequired["str"]
    """<p>The Amazon Web Services Glue version in the Spark Amazon Web Services Glue properties.</p>"""
    idle_timeout: NotRequired["int"]
    """<p>The idle timeout in the Spark Amazon Web Services Glue properties.</p>"""
    java_virtual_env: NotRequired["str"]
    """<p>The Java virtual env in the Spark Amazon Web Services Glue properties. </p>"""
    number_of_workers: NotRequired["int"]
    """<p>The number of workers in the Spark Amazon Web Services Glue properties. </p>"""
    python_virtual_env: NotRequired["str"]
    """<p>The Python virtual env in the Spark Amazon Web Services Glue properties. </p>"""
    worker_type: NotRequired["str"]
    """<p>The worker type in the Spark Amazon Web Services Glue properties. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkGluePropertiesInput) -> dict:
    out: dict = {}
    if "additional_args" in value:
        import aws_sdk_datazone.types.spark_glue_args

        out["additionalArgs"] = aws_sdk_datazone.types.spark_glue_args.serialize_json(
            value["additional_args"]
        )
    if "glue_connection_name" in value:
        out["glueConnectionName"] = value["glue_connection_name"]
    if "glue_connection_names" in value:
        import aws_sdk_datazone.types.glue_connection_names

        out["glueConnectionNames"] = (
            aws_sdk_datazone.types.glue_connection_names.serialize_json(
                value["glue_connection_names"]
            )
        )
    if "glue_version" in value:
        out["glueVersion"] = value["glue_version"]
    if "idle_timeout" in value:
        out["idleTimeout"] = value["idle_timeout"]
    if "java_virtual_env" in value:
        out["javaVirtualEnv"] = value["java_virtual_env"]
    if "number_of_workers" in value:
        out["numberOfWorkers"] = value["number_of_workers"]
    if "python_virtual_env" in value:
        out["pythonVirtualEnv"] = value["python_virtual_env"]
    if "worker_type" in value:
        out["workerType"] = value["worker_type"]
    return out


def deserialize_json(data: dict) -> SparkGluePropertiesInput:
    out: SparkGluePropertiesInput = {}  # type: ignore[typeddict-item]
    if "additionalArgs" in data:
        import aws_sdk_datazone.types.spark_glue_args

        out["additional_args"] = (
            aws_sdk_datazone.types.spark_glue_args.deserialize_json(
                data["additionalArgs"]
            )
        )
    if "glueConnectionName" in data:
        out["glue_connection_name"] = data["glueConnectionName"]
    if "glueConnectionNames" in data:
        import aws_sdk_datazone.types.glue_connection_names

        out["glue_connection_names"] = (
            aws_sdk_datazone.types.glue_connection_names.deserialize_json(
                data["glueConnectionNames"]
            )
        )
    if "glueVersion" in data:
        out["glue_version"] = data["glueVersion"]
    if "idleTimeout" in data:
        out["idle_timeout"] = data["idleTimeout"]
    if "javaVirtualEnv" in data:
        out["java_virtual_env"] = data["javaVirtualEnv"]
    if "numberOfWorkers" in data:
        out["number_of_workers"] = data["numberOfWorkers"]
    if "pythonVirtualEnv" in data:
        out["python_virtual_env"] = data["pythonVirtualEnv"]
    if "workerType" in data:
        out["worker_type"] = data["workerType"]
    return out
