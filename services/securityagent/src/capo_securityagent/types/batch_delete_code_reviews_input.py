"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDeleteCodeReviewsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_id_list


class BatchDeleteCodeReviewsInput(TypedDict, closed=True):
    code_review_ids: "capo_securityagent.types.code_review_id_list.CodeReviewIdList"
    """<p>The list of code review identifiers to delete.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code reviews to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteCodeReviewsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.code_review_id_list

    out["codeReviewIds"] = capo_securityagent.types.code_review_id_list.serialize_json(
        value["code_review_ids"]
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchDeleteCodeReviewsInput:
    out: BatchDeleteCodeReviewsInput = {}  # type: ignore[typeddict-item]
    if "codeReviewIds" in data:
        import capo_securityagent.types.code_review_id_list

        out["code_review_ids"] = (
            capo_securityagent.types.code_review_id_list.deserialize_json(
                data["codeReviewIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteCodeReviewsInput.code_review_ids required"
        )
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "BatchDeleteCodeReviewsInput.agent_space_id required"
        )
    return out
