"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateTrustRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.selective_auth
    import aws_sdk_directory_service.types.trust_id


class UpdateTrustRequest(TypedDict):
    trust_id: "aws_sdk_directory_service.types.trust_id.TrustId"
    """<p>Identifier of the trust relationship.</p>"""
    selective_auth: NotRequired[
        "aws_sdk_directory_service.types.selective_auth.SelectiveAuth"
    ]
    """<p>Updates selective authentication for the trust.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrustRequest) -> dict:
    out: dict = {}
    out["TrustId"] = value["trust_id"]
    if "selective_auth" in value:
        import aws_sdk_directory_service.types.selective_auth

        out["SelectiveAuth"] = (
            aws_sdk_directory_service.types.selective_auth.serialize_aws_json_1_1(
                value["selective_auth"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrustRequest:
    out: UpdateTrustRequest = {}  # type: ignore[typeddict-item]
    if "TrustId" in data:
        out["trust_id"] = data["TrustId"]
    else:
        raise DeserializationError("UpdateTrustRequest.trust_id required")
    if "SelectiveAuth" in data:
        import aws_sdk_directory_service.types.selective_auth

        out["selective_auth"] = (
            aws_sdk_directory_service.types.selective_auth.deserialize_aws_json_1_1(
                data["SelectiveAuth"]
            )
        )
    return out
