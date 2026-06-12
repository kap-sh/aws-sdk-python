"""Generated from Smithy shape ``com.amazonaws.signer#StartSigningJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.account_id
    import aws_sdk_signer.types.client_request_token
    import aws_sdk_signer.types.destination
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.source


class StartSigningJobRequest(TypedDict):
    source: "aws_sdk_signer.types.source.Source"
    """<p>The S3 bucket that contains the object to sign or a BLOB that contains your raw code.</p>"""
    destination: "aws_sdk_signer.types.destination.Destination"
    """<p>The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.</p>"""
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile.</p>"""
    client_request_token: "aws_sdk_signer.types.client_request_token.ClientRequestToken"
    """<p>String that identifies the signing request. All calls after the first that use this token return the same response as the first call.</p>"""
    profile_owner: NotRequired["aws_sdk_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the signing profile owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSigningJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_signer.types.source

    out["source"] = aws_sdk_signer.types.source.serialize_json(value["source"])
    import aws_sdk_signer.types.destination

    out["destination"] = aws_sdk_signer.types.destination.serialize_json(
        value["destination"]
    )
    out["profileName"] = value["profile_name"]
    out["clientRequestToken"] = value["client_request_token"]
    if "profile_owner" in value:
        out["profileOwner"] = value["profile_owner"]
    return out


def deserialize_json(data: dict) -> StartSigningJobRequest:
    out: StartSigningJobRequest = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_signer.types.source

        out["source"] = aws_sdk_signer.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("StartSigningJobRequest.source required")
    if "destination" in data:
        import aws_sdk_signer.types.destination

        out["destination"] = aws_sdk_signer.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        raise DeserializationError("StartSigningJobRequest.destination required")
    if "profileName" in data:
        out["profile_name"] = data["profileName"]
    else:
        raise DeserializationError("StartSigningJobRequest.profile_name required")
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        raise DeserializationError(
            "StartSigningJobRequest.client_request_token required"
        )
    if "profileOwner" in data:
        out["profile_owner"] = data["profileOwner"]
    return out
