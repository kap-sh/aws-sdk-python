"""Generated from Smithy shape ``com.amazonaws.configservice#PutEvaluationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.evaluations


class PutEvaluationsResponse(TypedDict, closed=True):
    failed_evaluations: NotRequired["capo_config_service.types.evaluations.Evaluations"]
    """<p>Requests that failed because of a client or server error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEvaluationsResponse) -> dict:
    out: dict = {}
    if "failed_evaluations" in value:
        import capo_config_service.types.evaluations

        out["FailedEvaluations"] = (
            capo_config_service.types.evaluations.serialize_aws_json_1_1(
                value["failed_evaluations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEvaluationsResponse:
    out: PutEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if "FailedEvaluations" in data:
        import capo_config_service.types.evaluations

        out["failed_evaluations"] = (
            capo_config_service.types.evaluations.deserialize_aws_json_1_1(
                data["FailedEvaluations"]
            )
        )
    return out
