"""Generated from Smithy shape ``com.amazonaws.configservice#StartResourceEvaluationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_evaluation_id


class StartResourceEvaluationResponse(TypedDict, closed=True):
    resource_evaluation_id: NotRequired[
        "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    ]
    """<p>A unique ResourceEvaluationId that is associated with a single execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartResourceEvaluationResponse) -> dict:
    out: dict = {}
    if "resource_evaluation_id" in value:
        out["ResourceEvaluationId"] = value["resource_evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartResourceEvaluationResponse:
    out: StartResourceEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "ResourceEvaluationId" in data:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    return out
