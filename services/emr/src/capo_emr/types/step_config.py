"""Generated from Smithy shape ``com.amazonaws.emr#StepConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.action_on_failure
    import capo_emr.types.hadoop_jar_step_config
    import capo_emr.types.step_monitoring_configuration
    import capo_emr.types.xml_string_max_len256


class StepConfig(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the step.</p>"""
    action_on_failure: NotRequired["capo_emr.types.action_on_failure.ActionOnFailure"]
    """<p>The action to take when the step fails. Use one of the following values:</p> <ul> <li> <p> <code>TERMINATE_CLUSTER</code> - Shuts down the cluster.</p> </li> <li> <p> <code>CANCEL_AND_WAIT</code> - Cancels any pending steps and returns the cluster to the <code>WAITING</code> state.</p> </li> <li> <p> <code>CONTINUE</code> - Continues to the next step in the queue.</p> </li> <li> <p> <code>TERMINATE_JOB_FLOW</code> - Shuts down the cluster. <code>TERMINATE_JOB_FLOW</code> is provided for backward compatibility. We recommend using <code>TERMINATE_CLUSTER</code> instead.</p> </li> </ul> <p>If a cluster's <code>StepConcurrencyLevel</code> is greater than <code>1</code>, do not use <code>AddJobFlowSteps</code> to submit a step with this parameter set to <code>CANCEL_AND_WAIT</code> or <code>TERMINATE_CLUSTER</code>. The step is not submitted and the action fails with a message that the <code>ActionOnFailure</code> setting is not valid.</p> <p>If you change a cluster's <code>StepConcurrencyLevel</code> to be greater than 1 while a step is running, the <code>ActionOnFailure</code> parameter may not behave as you expect. In this case, for a step that fails with this parameter set to <code>CANCEL_AND_WAIT</code>, pending steps and the running step are not canceled; for a step that fails with this parameter set to <code>TERMINATE_CLUSTER</code>, the cluster does not terminate.</p>"""
    hadoop_jar_step: NotRequired[
        "capo_emr.types.hadoop_jar_step_config.HadoopJarStepConfig"
    ]
    """<p>The JAR file used for the step.</p>"""
    step_monitoring_configuration: NotRequired[
        "capo_emr.types.step_monitoring_configuration.StepMonitoringConfiguration"
    ]
    """<p>Object that holds configuration properties for logging.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "action_on_failure" in value:
        import capo_emr.types.action_on_failure

        out["ActionOnFailure"] = (
            capo_emr.types.action_on_failure.serialize_aws_json_1_1(
                value["action_on_failure"]
            )
        )
    if "hadoop_jar_step" in value:
        import capo_emr.types.hadoop_jar_step_config

        out["HadoopJarStep"] = (
            capo_emr.types.hadoop_jar_step_config.serialize_aws_json_1_1(
                value["hadoop_jar_step"]
            )
        )
    if "step_monitoring_configuration" in value:
        import capo_emr.types.step_monitoring_configuration

        out["StepMonitoringConfiguration"] = (
            capo_emr.types.step_monitoring_configuration.serialize_aws_json_1_1(
                value["step_monitoring_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepConfig:
    out: StepConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ActionOnFailure" in data:
        import capo_emr.types.action_on_failure

        out["action_on_failure"] = (
            capo_emr.types.action_on_failure.deserialize_aws_json_1_1(
                data["ActionOnFailure"]
            )
        )
    if "HadoopJarStep" in data:
        import capo_emr.types.hadoop_jar_step_config

        out["hadoop_jar_step"] = (
            capo_emr.types.hadoop_jar_step_config.deserialize_aws_json_1_1(
                data["HadoopJarStep"]
            )
        )
    if "StepMonitoringConfiguration" in data:
        import capo_emr.types.step_monitoring_configuration

        out["step_monitoring_configuration"] = (
            capo_emr.types.step_monitoring_configuration.deserialize_aws_json_1_1(
                data["StepMonitoringConfiguration"]
            )
        )
    return out
