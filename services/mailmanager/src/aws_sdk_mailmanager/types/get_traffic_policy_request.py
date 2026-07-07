"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetTrafficPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.traffic_policy_id


class GetTrafficPolicyRequest(TypedDict, closed=True):
    traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTrafficPolicyRequest) -> dict:
    out: dict = {}
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTrafficPolicyRequest:
    out: GetTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        raise DeserializationError("GetTrafficPolicyRequest.traffic_policy_id required")
    return out
