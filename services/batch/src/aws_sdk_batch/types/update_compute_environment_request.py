"""Generated from Smithy shape ``com.amazonaws.batch#UpdateComputeEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.ce_state
    import aws_sdk_batch.types.compute_resource_update
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.update_policy


class UpdateComputeEnvironmentRequest(TypedDict, closed=True):
    compute_environment: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or full Amazon Resource Name (ARN) of the compute environment to update.</p>"""
    state: NotRequired["aws_sdk_batch.types.ce_state.CEState"]
    """<p>The state of the compute environment. Compute environments in the <code>ENABLED</code> state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.</p> <p>If the state is <code>ENABLED</code>, then the Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.</p> <p>If the state is <code>DISABLED</code>, then the Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a <code>STARTING</code> or <code>RUNNING</code> state continue to progress normally. Managed compute environments in the <code>DISABLED</code> state don't scale out. </p> <note> <p>Compute environments in a <code>DISABLED</code> state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero <code>minvCpus</code> setting. To prevent additional charges, disable and delete the compute environment.</p> </note> <p>When an instance is idle, the instance scales down to the <code>minvCpus</code> value. However, the instance size doesn't change. For example, consider a <code>c5.8xlarge</code> instance with a <code>minvCpus</code> value of <code>4</code> and a <code>desiredvCpus</code> value of <code>36</code>. This instance doesn't scale down to a <code>c5.large</code> instance.</p>"""
    unmanagedv_cpus: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum number of vCPUs expected to be used for an unmanaged compute environment. Don't specify this parameter for a managed compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair-share job queue, no vCPU capacity is reserved.</p>"""
    compute_resources: NotRequired[
        "aws_sdk_batch.types.compute_resource_update.ComputeResourceUpdate"
    ]
    r"""<p>Details of the compute resources managed by the compute environment. Required for a managed compute environment. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html\">Compute Environments</a> in the <i>Batch User Guide</i>.</p>"""
    service_role: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The full Amazon Resource Name (ARN) of the IAM role that allows Batch to make calls to other Amazon Web Services services on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html\">Batch service IAM role</a> in the <i>Batch User Guide</i>.</p> <important> <p>If the compute environment has a service-linked role, it can't be changed to use a regular IAM role. Likewise, if the compute environment has a regular IAM role, it can't be changed to use a service-linked role. To update the parameters for the compute environment that require an infrastructure update to change, the <b>AWSServiceRoleForBatch</b> service-linked role must be used. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html\">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (recommended) or prefix the role name with the path.</p> <note> <p>Depending on how you created your Batch service role, its ARN might contain the <code>service-role</code> path prefix. When you only specify the name of the service role, Batch assumes that your ARN doesn't use the <code>service-role</code> path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.</p> </note>"""
    update_policy: NotRequired["aws_sdk_batch.types.update_policy.UpdatePolicy"]
    r"""<p>Specifies the updated infrastructure update policy for the compute environment. For more information about infrastructure updates, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html\">Updating compute environments</a> in the <i>Batch User Guide</i>.</p>"""
    context: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Reserved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComputeEnvironmentRequest) -> dict:
    out: dict = {}
    if "compute_environment" in value:
        out["computeEnvironment"] = value["compute_environment"]
    if "state" in value:
        import aws_sdk_batch.types.ce_state

        out["state"] = aws_sdk_batch.types.ce_state.serialize_json(value["state"])
    if "unmanagedv_cpus" in value:
        out["unmanagedvCpus"] = value["unmanagedv_cpus"]
    if "compute_resources" in value:
        import aws_sdk_batch.types.compute_resource_update

        out["computeResources"] = (
            aws_sdk_batch.types.compute_resource_update.serialize_json(
                value["compute_resources"]
            )
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "update_policy" in value:
        import aws_sdk_batch.types.update_policy

        out["updatePolicy"] = aws_sdk_batch.types.update_policy.serialize_json(
            value["update_policy"]
        )
    if "context" in value:
        out["context"] = value["context"]
    return out


def deserialize_json(data: dict) -> UpdateComputeEnvironmentRequest:
    out: UpdateComputeEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "computeEnvironment" in data:
        out["compute_environment"] = data["computeEnvironment"]
    if "state" in data:
        import aws_sdk_batch.types.ce_state

        out["state"] = aws_sdk_batch.types.ce_state.deserialize_json(data["state"])
    if "unmanagedvCpus" in data:
        out["unmanagedv_cpus"] = data["unmanagedvCpus"]
    if "computeResources" in data:
        import aws_sdk_batch.types.compute_resource_update

        out["compute_resources"] = (
            aws_sdk_batch.types.compute_resource_update.deserialize_json(
                data["computeResources"]
            )
        )
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "updatePolicy" in data:
        import aws_sdk_batch.types.update_policy

        out["update_policy"] = aws_sdk_batch.types.update_policy.deserialize_json(
            data["updatePolicy"]
        )
    if "context" in data:
        out["context"] = data["context"]
    return out
