"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_id_list


class BatchGetCodeReviewsInput(TypedDict, closed=True):
    code_review_ids: "aws_sdk_securityagent.types.code_review_id_list.CodeReviewIdList"
    """<p>The list of code review identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code reviews.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewsInput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.code_review_id_list

    out["codeReviewIds"] = (
        aws_sdk_securityagent.types.code_review_id_list.serialize_json(
            value["code_review_ids"]
        )
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewsInput:
    out: BatchGetCodeReviewsInput = {}  # type: ignore[typeddict-item]
    if "codeReviewIds" in data:
        import aws_sdk_securityagent.types.code_review_id_list

        out["code_review_ids"] = (
            aws_sdk_securityagent.types.code_review_id_list.deserialize_json(
                data["codeReviewIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetCodeReviewsInput.code_review_ids required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("BatchGetCodeReviewsInput.agent_space_id required")
    return out
