"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteTrafficPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.traffic_policy_id


class DeleteTrafficPolicyRequest(TypedDict, closed=True):
    traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTrafficPolicyRequest) -> dict:
    out: dict = {}
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTrafficPolicyRequest:
    out: DeleteTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        raise DeserializationError(
            "DeleteTrafficPolicyRequest.traffic_policy_id required"
        )
    return out
