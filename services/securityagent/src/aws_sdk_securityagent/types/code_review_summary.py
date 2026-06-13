"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class CodeReviewSummary(TypedDict):
    code_review_id: "str"
    """<p>The unique identifier of the code review.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code review.</p>"""
    title: "str"
    """<p>The title of the code review.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewSummary) -> dict:
    out: dict = {}
    out["codeReviewId"] = value["code_review_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["title"] = value["title"]
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


def deserialize_json(data: dict) -> CodeReviewSummary:
    out: CodeReviewSummary = {}  # type: ignore[typeddict-item]
    if "codeReviewId" in data:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("CodeReviewSummary.code_review_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("CodeReviewSummary.agent_space_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CodeReviewSummary.title required")
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
