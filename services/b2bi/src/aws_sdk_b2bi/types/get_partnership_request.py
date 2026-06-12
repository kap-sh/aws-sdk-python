"""Generated from Smithy shape ``com.amazonaws.b2bi#GetPartnershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.partnership_id


class GetPartnershipRequest(TypedDict):
    partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId"
    """<p>Specifies the unique, system-generated identifier for a partnership.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPartnershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPartnershipRequest:
    out: GetPartnershipRequest = {}  # type: ignore[typeddict-item]
    return out
