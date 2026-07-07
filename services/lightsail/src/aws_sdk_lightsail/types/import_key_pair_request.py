"""Generated from Smithy shape ``com.amazonaws.lightsail#ImportKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.base64
    import aws_sdk_lightsail.types.resource_name


class ImportKeyPairRequest(TypedDict, closed=True):
    key_pair_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the key pair for which you want to import the public key.</p>"""
    public_key_base64: "aws_sdk_lightsail.types.base64.Base64"
    """<p>A base64-encoded public key of the <code>ssh-rsa</code> type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportKeyPairRequest) -> dict:
    out: dict = {}
    out["keyPairName"] = value["key_pair_name"]
    out["publicKeyBase64"] = value["public_key_base64"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportKeyPairRequest:
    out: ImportKeyPairRequest = {}  # type: ignore[typeddict-item]
    if "keyPairName" in data:
        out["key_pair_name"] = data["keyPairName"]
    else:
        raise DeserializationError("ImportKeyPairRequest.key_pair_name required")
    if "publicKeyBase64" in data:
        out["public_key_base64"] = data["publicKeyBase64"]
    else:
        raise DeserializationError("ImportKeyPairRequest.public_key_base64 required")
    return out
