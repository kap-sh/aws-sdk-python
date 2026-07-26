"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateCodeReviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.assets
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.code_remediation_strategy
    import capo_securityagent.types.service_role


class CreateCodeReviewOutput(TypedDict, closed=True):
    code_review_id: "str"
    """<p>The unique identifier of the created code review.</p>"""
    title: NotRequired["str"]
    """<p>The title of the code review.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was last updated, in UTC format.</p>"""
    assets: NotRequired["capo_securityagent.types.assets.Assets"]
    """<p>The assets included in the code review.</p>"""
    service_role: NotRequired["capo_securityagent.types.service_role.ServiceRole"]
    """<p>The IAM service role used for the code review.</p>"""
    log_config: NotRequired["capo_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the code review.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space that contains the code review.</p>"""
    code_remediation_strategy: NotRequired[
        "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The code remediation strategy for the code review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeReviewOutput) -> dict:
    out: dict = {}
    out["codeReviewId"] = value["code_review_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "created_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["createdAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.serialize_json(value["assets"])
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import capo_securityagent.types.cloud_watch_log

        out["logConfig"] = capo_securityagent.types.cloud_watch_log.serialize_json(
            value["log_config"]
        )
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "code_remediation_strategy" in value:
        import capo_securityagent.types.code_remediation_strategy

        out["codeRemediationStrategy"] = (
            capo_securityagent.types.code_remediation_strategy.serialize_json(
                value["code_remediation_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCodeReviewOutput:
    out: CreateCodeReviewOutput = {}  # type: ignore[typeddict-item]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("CreateCodeReviewOutput.code_review_id required")
    if "title" in data:
        out["title"] = data["title"]
    if "createdAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["created_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "assets" in data:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.deserialize_json(data["assets"])
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "logConfig" in data:
        import capo_securityagent.types.cloud_watch_log

        out["log_config"] = capo_securityagent.types.cloud_watch_log.deserialize_json(
            data["logConfig"]
        )
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    if "codeRemediationStrategy" in data:
        import capo_securityagent.types.code_remediation_strategy

        out["code_remediation_strategy"] = (
            capo_securityagent.types.code_remediation_strategy.deserialize_json(
                data["codeRemediationStrategy"]
            )
        )
    return out
