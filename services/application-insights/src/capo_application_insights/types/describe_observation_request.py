"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeObservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.observation_id


class DescribeObservationRequest(TypedDict, closed=True):
    observation_id: "capo_application_insights.types.observation_id.ObservationId"
    """<p>The ID of the observation.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeObservationRequest) -> dict:
    out: dict = {}
    out["ObservationId"] = value["observation_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeObservationRequest:
    out: DescribeObservationRequest = {}  # type: ignore[typeddict-item]
    if "ObservationId" in data:
        out["observation_id"] = data["ObservationId"]
    else:
        raise DeserializationError("DescribeObservationRequest.observation_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
