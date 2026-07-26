"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DisableFederationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_arn


class DisableFederationRequest(TypedDict, closed=True):
    event_data_store: "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p> The ARN (or ID suffix of the ARN) of the event data store for which you want to disable Lake query federation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableFederationRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableFederationRequest:
    out: DisableFederationRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    else:
        raise DeserializationError("DisableFederationRequest.event_data_store required")
    return out
