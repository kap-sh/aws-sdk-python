"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateCodeReviewInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.assets
    import aws_sdk_securityagent.types.cloud_watch_log
    import aws_sdk_securityagent.types.code_remediation_strategy
    import aws_sdk_securityagent.types.service_role


class UpdateCodeReviewInput(TypedDict):
    code_review_id: "str"
    """<p>The unique identifier of the code review to update.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code review.</p>"""
    title: NotRequired["str"]
    """<p>The updated title of the code review.</p>"""
    assets: NotRequired["aws_sdk_securityagent.types.assets.Assets"]
    """<p>The updated assets for the code review.</p>"""
    service_role: NotRequired["aws_sdk_securityagent.types.service_role.ServiceRole"]
    """<p>The updated IAM service role for the code review.</p>"""
    log_config: NotRequired["aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The updated CloudWatch Logs configuration for the code review.</p>"""
    code_remediation_strategy: NotRequired[
        "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The updated code remediation strategy for the code review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeReviewInput) -> dict:
    out: dict = {}
    out["codeReviewId"] = value["code_review_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "assets" in value:
        import aws_sdk_securityagent.types.assets

        out["assets"] = aws_sdk_securityagent.types.assets.serialize_json(
            value["assets"]
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import aws_sdk_securityagent.types.cloud_watch_log

        out["logConfig"] = aws_sdk_securityagent.types.cloud_watch_log.serialize_json(
            value["log_config"]
        )
    if "code_remediation_strategy" in value:
        import aws_sdk_securityagent.types.code_remediation_strategy

        out["codeRemediationStrategy"] = (
            aws_sdk_securityagent.types.code_remediation_strategy.serialize_json(
                value["code_remediation_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCodeReviewInput:
    out: UpdateCodeReviewInput = {}  # type: ignore[typeddict-item]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("UpdateCodeReviewInput.code_review_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("UpdateCodeReviewInput.agent_space_id required")
    if "title" in data:
        out["title"] = data["title"]
    if "assets" in data:
        import aws_sdk_securityagent.types.assets

        out["assets"] = aws_sdk_securityagent.types.assets.deserialize_json(
            data["assets"]
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
    if "codeRemediationStrategy" in data:
        import aws_sdk_securityagent.types.code_remediation_strategy

        out["code_remediation_strategy"] = (
            aws_sdk_securityagent.types.code_remediation_strategy.deserialize_json(
                data["codeRemediationStrategy"]
            )
        )
    return out
