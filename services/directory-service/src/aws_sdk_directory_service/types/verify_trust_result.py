"""Generated from Smithy shape ``com.amazonaws.directoryservice#VerifyTrustResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.trust_id


class VerifyTrustResult(TypedDict, closed=True):
    trust_id: NotRequired["aws_sdk_directory_service.types.trust_id.TrustId"]
    """<p>The unique Trust ID of the trust relationship that was verified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyTrustResult) -> dict:
    out: dict = {}
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyTrustResult:
    out: VerifyTrustResult = {}  # type: ignore[typeddict-item]
    if "TrustId" in data:
        out["trust_id"] = data["TrustId"]
    return out
