"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateCodeReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.assets
    import aws_sdk_securityagent.types.cloud_watch_log
    import aws_sdk_securityagent.types.code_remediation_strategy
    import aws_sdk_securityagent.types.service_role


class CreateCodeReviewInput(TypedDict, closed=True):
    title: "str"
    """<p>The title of the code review.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space to create the code review in.</p>"""
    assets: "aws_sdk_securityagent.types.assets.Assets"
    """<p>The assets to include in the code review, such as documents and source code.</p>"""
    service_role: NotRequired["aws_sdk_securityagent.types.service_role.ServiceRole"]
    """<p>The IAM service role to use for the code review.</p>"""
    log_config: NotRequired["aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the code review.</p>"""
    code_remediation_strategy: NotRequired[
        "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The code remediation strategy for the code review. Valid values are AUTOMATIC and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeReviewInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_securityagent.types.assets

    out["assets"] = aws_sdk_securityagent.types.assets.serialize_json(value["assets"])
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


def deserialize_json(data: dict) -> CreateCodeReviewInput:
    out: CreateCodeReviewInput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateCodeReviewInput.title required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("CreateCodeReviewInput.agent_space_id required")
    if "assets" in data:
        import aws_sdk_securityagent.types.assets

        out["assets"] = aws_sdk_securityagent.types.assets.deserialize_json(
            data["assets"]
        )
    else:
        raise DeserializationError("CreateCodeReviewInput.assets required")
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
