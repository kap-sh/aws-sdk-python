"""Generated from Smithy shape ``com.amazonaws.emr#StepSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.action_on_failure
    import capo_emr.types.hadoop_step_config
    import capo_emr.types.step_id
    import capo_emr.types.step_status
    import capo_emr.types.string


class StepSummary(TypedDict, closed=True):
    id: NotRequired["capo_emr.types.step_id.StepId"]
    """<p>The identifier of the cluster step.</p>"""
    name: NotRequired["capo_emr.types.string.String"]
    """<p>The name of the cluster step.</p>"""
    config: NotRequired["capo_emr.types.hadoop_step_config.HadoopStepConfig"]
    """<p>The Hadoop job configuration of the cluster step.</p>"""
    action_on_failure: NotRequired["capo_emr.types.action_on_failure.ActionOnFailure"]
    """<p>The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is available for backward compatibility.</p>"""
    status: NotRequired["capo_emr.types.step_status.StepStatus"]
    """<p>The current execution status details of the cluster step.</p>"""
    log_uri: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon S3 destination URI for log publishing.</p>"""
    encryption_key_arn: NotRequired["capo_emr.types.string.String"]
    """<p>The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "config" in value:
        import capo_emr.types.hadoop_step_config

        out["Config"] = capo_emr.types.hadoop_step_config.serialize_aws_json_1_1(
            value["config"]
        )
    if "action_on_failure" in value:
        import capo_emr.types.action_on_failure

        out["ActionOnFailure"] = (
            capo_emr.types.action_on_failure.serialize_aws_json_1_1(
                value["action_on_failure"]
            )
        )
    if "status" in value:
        import capo_emr.types.step_status

        out["Status"] = capo_emr.types.step_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StepSummary:
    out: StepSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Config" in data:
        import capo_emr.types.hadoop_step_config

        out["config"] = capo_emr.types.hadoop_step_config.deserialize_aws_json_1_1(
            data["Config"]
        )
    if "ActionOnFailure" in data:
        import capo_emr.types.action_on_failure

        out["action_on_failure"] = (
            capo_emr.types.action_on_failure.deserialize_aws_json_1_1(
                data["ActionOnFailure"]
            )
        )
    if "Status" in data:
        import capo_emr.types.step_status

        out["status"] = capo_emr.types.step_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "LogUri" in data:
        out["log_uri"] = data["LogUri"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
