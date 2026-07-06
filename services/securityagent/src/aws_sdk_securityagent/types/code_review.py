"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.assets
    import aws_sdk_securityagent.types.cloud_watch_log
    import aws_sdk_securityagent.types.code_remediation_strategy
    import aws_sdk_securityagent.types.service_role


class CodeReview(TypedDict, closed=True):
    code_review_id: "str"
    """<p>The unique identifier of the code review.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code review.</p>"""
    title: "str"
    """<p>The title of the code review.</p>"""
    assets: "aws_sdk_securityagent.types.assets.Assets"
    """<p>The assets included in the code review.</p>"""
    service_role: NotRequired["aws_sdk_securityagent.types.service_role.ServiceRole"]
    """<p>The IAM service role used for the code review.</p>"""
    log_config: NotRequired["aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the code review.</p>"""
    code_remediation_strategy: NotRequired[
        "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The code remediation strategy for the code review.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReview) -> dict:
    out: dict = {}
    out["codeReviewId"] = value["code_review_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["title"] = value["title"]
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


def deserialize_json(data: dict) -> CodeReview:
    out: CodeReview = {}  # type: ignore[typeddict-item]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("CodeReview.code_review_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("CodeReview.agent_space_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CodeReview.title required")
    if "assets" in data:
        import aws_sdk_securityagent.types.assets

        out["assets"] = aws_sdk_securityagent.types.assets.deserialize_json(
            data["assets"]
        )
    else:
        raise DeserializationError("CodeReview.assets required")
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
