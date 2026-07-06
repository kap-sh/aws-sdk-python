"""Generated from Smithy shape ``com.amazonaws.batch#UpdateJobQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.compute_environment_orders
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.job_state_time_limit_actions
    import aws_sdk_batch.types.jq_state
    import aws_sdk_batch.types.service_environment_orders
    import aws_sdk_batch.types.string


class UpdateJobQueueRequest(TypedDict, closed=True):
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or the Amazon Resource Name (ARN) of the job queue.</p>"""
    state: NotRequired["aws_sdk_batch.types.jq_state.JQState"]
    """<p>Describes the queue's ability to accept new jobs. If the job queue state is <code>ENABLED</code>, it can accept jobs. If the job queue state is <code>DISABLED</code>, new jobs can't be added to the queue, but jobs already in the queue can finish.</p>"""
    scheduling_policy_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the fair-share scheduling policy. Once a job queue is created, the fair-share scheduling policy can be replaced but not removed. The format is <code>aws:<i>Partition</i>:batch:<i>Region</i>:<i>Account</i>:scheduling-policy/<i>Name</i> </code>. For example, <code>aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy</code>.</p>"""
    priority: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The priority of the job queue. Job queues with a higher priority (or a higher integer value for the <code>priority</code> parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of <code>10</code> is given scheduling preference over a job queue with a priority value of <code>1</code>. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>). EC2 and Fargate compute environments can't be mixed.</p>"""
    compute_environment_order: NotRequired[
        "aws_sdk_batch.types.compute_environment_orders.ComputeEnvironmentOrders"
    ]
    """<p>Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment runs a given job. Compute environments must be in the <code>VALID</code> state before you can associate them with a job queue. All of the compute environments must be either EC2 (<code>EC2</code> or <code>SPOT</code>) or Fargate (<code>FARGATE</code> or <code>FARGATE_SPOT</code>). EC2 and Fargate compute environments can't be mixed.</p> <note> <p>All compute environments that are associated with a job queue must share the same architecture. Batch doesn't support mixing compute environment architecture types in a single job queue.</p> </note>"""
    service_environment_order: NotRequired[
        "aws_sdk_batch.types.service_environment_orders.ServiceEnvironmentOrders"
    ]
    """<p>The order of the service environment associated with the job queue. Job queues with a higher priority are evaluated first when associated with the same service environment.</p>"""
    job_state_time_limit_actions: NotRequired[
        "aws_sdk_batch.types.job_state_time_limit_actions.JobStateTimeLimitActions"
    ]
    """<p>The set of actions that Batch perform on jobs that remain at the head of the job queue in the specified state longer than specified times. Batch will perform each action after <code>maxTimeSeconds</code> has passed. (<b>Note</b>: The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobQueueRequest) -> dict:
    out: dict = {}
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "state" in value:
        import aws_sdk_batch.types.jq_state

        out["state"] = aws_sdk_batch.types.jq_state.serialize_json(value["state"])
    if "scheduling_policy_arn" in value:
        out["schedulingPolicyArn"] = value["scheduling_policy_arn"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "compute_environment_order" in value:
        import aws_sdk_batch.types.compute_environment_orders

        out["computeEnvironmentOrder"] = (
            aws_sdk_batch.types.compute_environment_orders.serialize_json(
                value["compute_environment_order"]
            )
        )
    if "service_environment_order" in value:
        import aws_sdk_batch.types.service_environment_orders

        out["serviceEnvironmentOrder"] = (
            aws_sdk_batch.types.service_environment_orders.serialize_json(
                value["service_environment_order"]
            )
        )
    if "job_state_time_limit_actions" in value:
        import aws_sdk_batch.types.job_state_time_limit_actions

        out["jobStateTimeLimitActions"] = (
            aws_sdk_batch.types.job_state_time_limit_actions.serialize_json(
                value["job_state_time_limit_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateJobQueueRequest:
    out: UpdateJobQueueRequest = {}  # type: ignore[typeddict-item]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "state" in data:
        import aws_sdk_batch.types.jq_state

        out["state"] = aws_sdk_batch.types.jq_state.deserialize_json(data["state"])
    if "schedulingPolicyArn" in data:
        out["scheduling_policy_arn"] = data["schedulingPolicyArn"]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "computeEnvironmentOrder" in data:
        import aws_sdk_batch.types.compute_environment_orders

        out["compute_environment_order"] = (
            aws_sdk_batch.types.compute_environment_orders.deserialize_json(
                data["computeEnvironmentOrder"]
            )
        )
    if "serviceEnvironmentOrder" in data:
        import aws_sdk_batch.types.service_environment_orders

        out["service_environment_order"] = (
            aws_sdk_batch.types.service_environment_orders.deserialize_json(
                data["serviceEnvironmentOrder"]
            )
        )
    if "jobStateTimeLimitActions" in data:
        import aws_sdk_batch.types.job_state_time_limit_actions

        out["job_state_time_limit_actions"] = (
            aws_sdk_batch.types.job_state_time_limit_actions.deserialize_json(
                data["jobStateTimeLimitActions"]
            )
        )
    return out
