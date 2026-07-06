"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.cloud_watch_log
    import aws_sdk_securityagent.types.code_remediation_strategy
    import aws_sdk_securityagent.types.document_list
    import aws_sdk_securityagent.types.error_information
    import aws_sdk_securityagent.types.execution_context_list
    import aws_sdk_securityagent.types.integrated_repository_list
    import aws_sdk_securityagent.types.job_status
    import aws_sdk_securityagent.types.service_role
    import aws_sdk_securityagent.types.source_code_repository_list
    import aws_sdk_securityagent.types.step_list


class CodeReviewJob(TypedDict, closed=True):
    code_review_job_id: NotRequired["str"]
    """<p>The unique identifier of the code review job.</p>"""
    code_review_id: NotRequired["str"]
    """<p>The unique identifier of the code review associated with the job.</p>"""
    title: NotRequired["str"]
    """<p>The title of the code review job.</p>"""
    overview: NotRequired["str"]
    """<p>An overview of the code review job results.</p>"""
    status: NotRequired["aws_sdk_securityagent.types.job_status.JobStatus"]
    """<p>The current status of the code review job.</p>"""
    documents: NotRequired["aws_sdk_securityagent.types.document_list.DocumentList"]
    """<p>The list of documents providing context for the code review job.</p>"""
    source_code: NotRequired[
        "aws_sdk_securityagent.types.source_code_repository_list.SourceCodeRepositoryList"
    ]
    """<p>The list of source code repositories analyzed during the code review job.</p>"""
    steps: NotRequired["aws_sdk_securityagent.types.step_list.StepList"]
    """<p>The list of steps in the code review job execution.</p>"""
    execution_context: NotRequired[
        "aws_sdk_securityagent.types.execution_context_list.ExecutionContextList"
    ]
    """<p>The execution context messages for the code review job.</p>"""
    service_role: NotRequired["aws_sdk_securityagent.types.service_role.ServiceRole"]
    """<p>The IAM service role used for the code review job.</p>"""
    log_config: NotRequired["aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the code review job.</p>"""
    error_information: NotRequired[
        "aws_sdk_securityagent.types.error_information.ErrorInformation"
    ]
    """<p>Error information if the code review job encountered an error.</p>"""
    integrated_repositories: NotRequired[
        "aws_sdk_securityagent.types.integrated_repository_list.IntegratedRepositoryList"
    ]
    """<p>The list of integrated repositories associated with the code review job.</p>"""
    code_remediation_strategy: NotRequired[
        "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The code remediation strategy for the code review job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review job was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review job was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJob) -> dict:
    out: dict = {}
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    if "code_review_id" in value:
        out["codeReviewId"] = value["code_review_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "overview" in value:
        out["overview"] = value["overview"]
    if "status" in value:
        import aws_sdk_securityagent.types.job_status

        out["status"] = aws_sdk_securityagent.types.job_status.serialize_json(
            value["status"]
        )
    if "documents" in value:
        import aws_sdk_securityagent.types.document_list

        out["documents"] = aws_sdk_securityagent.types.document_list.serialize_json(
            value["documents"]
        )
    if "source_code" in value:
        import aws_sdk_securityagent.types.source_code_repository_list

        out["sourceCode"] = (
            aws_sdk_securityagent.types.source_code_repository_list.serialize_json(
                value["source_code"]
            )
        )
    if "steps" in value:
        import aws_sdk_securityagent.types.step_list

        out["steps"] = aws_sdk_securityagent.types.step_list.serialize_json(
            value["steps"]
        )
    if "execution_context" in value:
        import aws_sdk_securityagent.types.execution_context_list

        out["executionContext"] = (
            aws_sdk_securityagent.types.execution_context_list.serialize_json(
                value["execution_context"]
            )
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import aws_sdk_securityagent.types.cloud_watch_log

        out["logConfig"] = aws_sdk_securityagent.types.cloud_watch_log.serialize_json(
            value["log_config"]
        )
    if "error_information" in value:
        import aws_sdk_securityagent.types.error_information

        out["errorInformation"] = (
            aws_sdk_securityagent.types.error_information.serialize_json(
                value["error_information"]
            )
        )
    if "integrated_repositories" in value:
        import aws_sdk_securityagent.types.integrated_repository_list

        out["integratedRepositories"] = (
            aws_sdk_securityagent.types.integrated_repository_list.serialize_json(
                value["integrated_repositories"]
            )
        )
    if "code_remediation_strategy" in value:
        import aws_sdk_securityagent.types.code_remediation_strategy

        out["codeRemediationStrategy"] = (
            aws_sdk_securityagent.types.code_remediation_strategy.serialize_json(
                value["code_remediation_strategy"]
            )
        )
    if "created_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeReviewJob:
    out: CodeReviewJob = {}  # type: ignore[typeddict-item]
    if "codeReviewJobId" in data:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    if "title" in data:
        out["title"] = data["title"]
    if "overview" in data:
        out["overview"] = data["overview"]
    if "status" in data:
        import aws_sdk_securityagent.types.job_status

        out["status"] = aws_sdk_securityagent.types.job_status.deserialize_json(
            data["status"]
        )
    if "documents" in data:
        import aws_sdk_securityagent.types.document_list

        out["documents"] = aws_sdk_securityagent.types.document_list.deserialize_json(
            data["documents"]
        )
    if "sourceCode" in data:
        import aws_sdk_securityagent.types.source_code_repository_list

        out["source_code"] = (
            aws_sdk_securityagent.types.source_code_repository_list.deserialize_json(
                data["sourceCode"]
            )
        )
    if "steps" in data:
        import aws_sdk_securityagent.types.step_list

        out["steps"] = aws_sdk_securityagent.types.step_list.deserialize_json(
            data["steps"]
        )
    if "executionContext" in data:
        import aws_sdk_securityagent.types.execution_context_list

        out["execution_context"] = (
            aws_sdk_securityagent.types.execution_context_list.deserialize_json(
                data["executionContext"]
            )
        )
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "logConfig" in data:
        import aws_sdk_securityagent.types.cloud_watch_log

        out["log_config"] = (
            aws_sdk_securityagent.types.cloud_watch_log.deserialize_json(
                data["logConfig"]
            )
        )
    if "errorInformation" in data:
        import aws_sdk_securityagent.types.error_information

        out["error_information"] = (
            aws_sdk_securityagent.types.error_information.deserialize_json(
                data["errorInformation"]
            )
        )
    if "integratedRepositories" in data:
        import aws_sdk_securityagent.types.integrated_repository_list

        out["integrated_repositories"] = (
            aws_sdk_securityagent.types.integrated_repository_list.deserialize_json(
                data["integratedRepositories"]
            )
        )
    if "codeRemediationStrategy" in data:
        import aws_sdk_securityagent.types.code_remediation_strategy

        out["code_remediation_strategy"] = (
            aws_sdk_securityagent.types.code_remediation_strategy.deserialize_json(
                data["codeRemediationStrategy"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
