"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateTrustResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.request_id
    import aws_sdk_directory_service.types.trust_id


class UpdateTrustResult(TypedDict):
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]
    trust_id: NotRequired["aws_sdk_directory_service.types.trust_id.TrustId"]
    """<p>Identifier of the trust relationship.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrustResult) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrustResult:
    out: UpdateTrustResult = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "TrustId" in data:
        out["trust_id"] = data["TrustId"]
    return out
