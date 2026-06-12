"""Generated from Smithy shape ``com.amazonaws.mturk#UpdateHITReviewStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.boolean
    import aws_sdk_mturk.types.entity_id


class UpdateHITReviewStatusRequest(TypedDict):
    hit_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p> The ID of the HIT to update. </p>"""
    revert: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p> Specifies how to update the HIT status. Default is <code>False</code>. </p> <ul> <li> <p> Setting this to false will only transition a HIT from <code>Reviewable</code> to <code>Reviewing</code> </p> </li> <li> <p> Setting this to true will only transition a HIT from <code>Reviewing</code> to <code>Reviewable</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHITReviewStatusRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    if "revert" in value:
        out["Revert"] = value["revert"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHITReviewStatusRequest:
    out: UpdateHITReviewStatusRequest = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    else:
        raise DeserializationError("UpdateHITReviewStatusRequest.hit_id required")
    if "Revert" in data:
        out["revert"] = data["Revert"]
    return out
