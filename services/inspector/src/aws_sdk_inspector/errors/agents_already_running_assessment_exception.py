"""Generated from Smithy shape ``com.amazonaws.inspector#AgentsAlreadyRunningAssessmentException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_already_running_assessment_list
    import aws_sdk_inspector.types.bool
    import aws_sdk_inspector.types.error_message


class AgentsAlreadyRunningAssessmentException_(TypedDict):
    message: "aws_sdk_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    agents: "aws_sdk_inspector.types.agent_already_running_assessment_list.AgentAlreadyRunningAssessmentList"
    """<p></p>"""
    agents_truncated: "aws_sdk_inspector.types.bool.Bool"
    """<p></p>"""
    can_retry: "aws_sdk_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentsAlreadyRunningAssessmentException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_inspector.types.agent_already_running_assessment_list

    out["agents"] = (
        aws_sdk_inspector.types.agent_already_running_assessment_list.serialize_aws_json_1_1(
            value["agents"]
        )
    )
    out["agentsTruncated"] = value["agents_truncated"]
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentsAlreadyRunningAssessmentException_:
    out: AgentsAlreadyRunningAssessmentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "AgentsAlreadyRunningAssessmentException_.message required"
        )
    if "agents" in data:
        import aws_sdk_inspector.types.agent_already_running_assessment_list

        out["agents"] = (
            aws_sdk_inspector.types.agent_already_running_assessment_list.deserialize_aws_json_1_1(
                data["agents"]
            )
        )
    else:
        raise DeserializationError(
            "AgentsAlreadyRunningAssessmentException_.agents required"
        )
    if "agentsTruncated" in data:
        out["agents_truncated"] = data["agentsTruncated"]
    else:
        raise DeserializationError(
            "AgentsAlreadyRunningAssessmentException_.agents_truncated required"
        )
    if "canRetry" in data:
        out["can_retry"] = data["canRetry"]
    else:
        raise DeserializationError(
            "AgentsAlreadyRunningAssessmentException_.can_retry required"
        )
    return out


class AgentsAlreadyRunningAssessmentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#AgentsAlreadyRunningAssessmentException``."""

    code: str | None = "AgentsAlreadyRunningAssessmentException"

    def __init__(self, data: AgentsAlreadyRunningAssessmentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AgentsAlreadyRunningAssessmentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AgentsAlreadyRunningAssessmentException":
        return cls(deserialize_aws_json_1_1(data))
