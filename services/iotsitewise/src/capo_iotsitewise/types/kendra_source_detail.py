"""Generated from Smithy shape ``com.amazonaws.iotsitewise#KendraSourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn


class KendraSourceDetail(TypedDict, closed=True):
    knowledge_base_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <code>knowledgeBaseArn</code> details for the Kendra dataset source.</p>"""
    role_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <code>roleARN</code> details for the Kendra dataset source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraSourceDetail) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> KendraSourceDetail:
    out: KendraSourceDetail = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("KendraSourceDetail.knowledge_base_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("KendraSourceDetail.role_arn required")
    return out
