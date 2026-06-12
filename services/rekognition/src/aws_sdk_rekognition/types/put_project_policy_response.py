"""Generated from Smithy shape ``com.amazonaws.rekognition#PutProjectPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_policy_revision_id


class PutProjectPolicyResponse(TypedDict):
    policy_revision_id: NotRequired[
        "aws_sdk_rekognition.types.project_policy_revision_id.ProjectPolicyRevisionId"
    ]
    """<p>The ID of the project policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutProjectPolicyResponse) -> dict:
    out: dict = {}
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutProjectPolicyResponse:
    out: PutProjectPolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
