"""Generated from Smithy shape ``com.amazonaws.signer#SignPayloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.account_id
    import aws_sdk_signer.types.payload
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.string


class SignPayloadRequest(TypedDict, closed=True):
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile.</p>"""
    profile_owner: NotRequired["aws_sdk_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the profile owner.</p>"""
    payload: "aws_sdk_signer.types.payload.Payload"
    """<p>Specifies the object digest (hash) to sign.</p>"""
    payload_format: "aws_sdk_signer.types.string.String"
    """<p>Payload content type. The single valid type is <code>application/vnd.cncf.notary.payload.v1+json</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignPayloadRequest) -> dict:
    out: dict = {}
    out["profileName"] = value["profile_name"]
    if "profile_owner" in value:
        out["profileOwner"] = value["profile_owner"]
    import aws_sdk_signer.types.payload

    out["payload"] = aws_sdk_signer.types.payload.serialize_json(value["payload"])
    out["payloadFormat"] = value["payload_format"]
    return out


def deserialize_json(data: dict) -> SignPayloadRequest:
    out: SignPayloadRequest = {}  # type: ignore[typeddict-item]
    if "profileName" in data:
        out["profile_name"] = data["profileName"]
    else:
        raise DeserializationError("SignPayloadRequest.profile_name required")
    if "profileOwner" in data:
        out["profile_owner"] = data["profileOwner"]
    if "payload" in data:
        import aws_sdk_signer.types.payload

        out["payload"] = aws_sdk_signer.types.payload.deserialize_json(data["payload"])
    else:
        raise DeserializationError("SignPayloadRequest.payload required")
    if "payloadFormat" in data:
        out["payload_format"] = data["payloadFormat"]
    else:
        raise DeserializationError("SignPayloadRequest.payload_format required")
    return out
