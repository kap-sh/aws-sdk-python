"""Generated from Smithy shape ``com.amazonaws.batch#SubmitServiceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.client_request_token
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.service_job_preemption_configuration
    import aws_sdk_batch.types.service_job_retry_strategy
    import aws_sdk_batch.types.service_job_timeout
    import aws_sdk_batch.types.service_job_type
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class SubmitServiceJobRequest(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the service job. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job queue into which the service job is submitted. You can specify either the name or the ARN of the queue. The job queue must have the type <code>SAGEMAKER_TRAINING</code>.</p>"""
    retry_strategy: NotRequired[
        "aws_sdk_batch.types.service_job_retry_strategy.ServiceJobRetryStrategy"
    ]
    """<p>The retry strategy to use for failed service jobs that are submitted with this service job request. </p>"""
    scheduling_priority: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The scheduling priority of the service job. Valid values are integers between 0 and 9999.</p>"""
    service_request_payload: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The request, in JSON, for the service that the SubmitServiceJob operation is queueing. </p>"""
    service_job_type: NotRequired["aws_sdk_batch.types.service_job_type.ServiceJobType"]
    """<p>The type of service job. For SageMaker Training jobs, specify <code>SAGEMAKER_TRAINING</code>.</p>"""
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The share identifier for the service job. Don't specify this parameter if the job queue doesn't have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.</p>"""
    quota_share_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The quota share for the service job. Don't specify this parameter if the job queue doesn't have a quota share scheduling policy. If the job queue has a quota share scheduling policy, then this parameter must be specified.</p>"""
    preemption_configuration: NotRequired[
        "aws_sdk_batch.types.service_job_preemption_configuration.ServiceJobPreemptionConfiguration"
    ]
    """<p>Specifies the service job behavior when preempted.</p>"""
    timeout_config: NotRequired[
        "aws_sdk_batch.types.service_job_timeout.ServiceJobTimeout"
    ]
    """<p>The timeout configuration for the service job. If none is specified, Batch defers to the default timeout of the underlying service handling the job.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    r"""<p>The tags that you apply to the service job request. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a>.</p>"""
    client_token: NotRequired[
        "aws_sdk_batch.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for the request. This token is used to ensure idempotency of requests. If this parameter is specified and two submit requests with identical payloads and <code>clientToken</code>s are received, these requests are considered the same request and the second request is rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitServiceJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "retry_strategy" in value:
        import aws_sdk_batch.types.service_job_retry_strategy

        out["retryStrategy"] = (
            aws_sdk_batch.types.service_job_retry_strategy.serialize_json(
                value["retry_strategy"]
            )
        )
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "service_request_payload" in value:
        out["serviceRequestPayload"] = value["service_request_payload"]
    if "service_job_type" in value:
        import aws_sdk_batch.types.service_job_type

        out["serviceJobType"] = aws_sdk_batch.types.service_job_type.serialize_json(
            value["service_job_type"]
        )
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "preemption_configuration" in value:
        import aws_sdk_batch.types.service_job_preemption_configuration

        out["preemptionConfiguration"] = (
            aws_sdk_batch.types.service_job_preemption_configuration.serialize_json(
                value["preemption_configuration"]
            )
        )
    if "timeout_config" in value:
        import aws_sdk_batch.types.service_job_timeout

        out["timeoutConfig"] = aws_sdk_batch.types.service_job_timeout.serialize_json(
            value["timeout_config"]
        )
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SubmitServiceJobRequest:
    out: SubmitServiceJobRequest = {}  # type: ignore[typeddict-item]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "retryStrategy" in data:
        import aws_sdk_batch.types.service_job_retry_strategy

        out["retry_strategy"] = (
            aws_sdk_batch.types.service_job_retry_strategy.deserialize_json(
                data["retryStrategy"]
            )
        )
    if "schedulingPriority" in data:
        out["scheduling_priority"] = data["schedulingPriority"]
    if "serviceRequestPayload" in data:
        out["service_request_payload"] = data["serviceRequestPayload"]
    if "serviceJobType" in data:
        import aws_sdk_batch.types.service_job_type

        out["service_job_type"] = aws_sdk_batch.types.service_job_type.deserialize_json(
            data["serviceJobType"]
        )
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "preemptionConfiguration" in data:
        import aws_sdk_batch.types.service_job_preemption_configuration

        out["preemption_configuration"] = (
            aws_sdk_batch.types.service_job_preemption_configuration.deserialize_json(
                data["preemptionConfiguration"]
            )
        )
    if "timeoutConfig" in data:
        import aws_sdk_batch.types.service_job_timeout

        out["timeout_config"] = (
            aws_sdk_batch.types.service_job_timeout.deserialize_json(
                data["timeoutConfig"]
            )
        )
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
