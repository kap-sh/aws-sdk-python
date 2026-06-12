"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateTrustResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.trust_id


class CreateTrustResult(TypedDict):
    trust_id: NotRequired["aws_sdk_directory_service.types.trust_id.TrustId"]
    """<p>A unique identifier for the trust relationship that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrustResult) -> dict:
    out: dict = {}
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrustResult:
    out: CreateTrustResult = {}  # type: ignore[typeddict-item]
    if "TrustId" in data:
        out["trust_id"] = data["TrustId"]
    return out
