"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateKeyPairResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.base64
    import aws_sdk_lightsail.types.key_pair
    import aws_sdk_lightsail.types.operation


class CreateKeyPairResult(TypedDict, closed=True):
    key_pair: NotRequired["aws_sdk_lightsail.types.key_pair.KeyPair"]
    """<p>An array of key-value pairs containing information about the new key pair you just created.</p>"""
    public_key_base64: NotRequired["aws_sdk_lightsail.types.base64.Base64"]
    """<p>A base64-encoded public key of the <code>ssh-rsa</code> type.</p>"""
    private_key_base64: NotRequired["aws_sdk_lightsail.types.base64.Base64"]
    """<p>A base64-encoded RSA private key.</p>"""
    operation: NotRequired["aws_sdk_lightsail.types.operation.Operation"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateKeyPairResult) -> dict:
    out: dict = {}
    if "key_pair" in value:
        import aws_sdk_lightsail.types.key_pair

        out["keyPair"] = aws_sdk_lightsail.types.key_pair.serialize_aws_json_1_1(
            value["key_pair"]
        )
    if "public_key_base64" in value:
        out["publicKeyBase64"] = value["public_key_base64"]
    if "private_key_base64" in value:
        out["privateKeyBase64"] = value["private_key_base64"]
    if "operation" in value:
        import aws_sdk_lightsail.types.operation

        out["operation"] = aws_sdk_lightsail.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateKeyPairResult:
    out: CreateKeyPairResult = {}  # type: ignore[typeddict-item]
    if "keyPair" in data:
        import aws_sdk_lightsail.types.key_pair

        out["key_pair"] = aws_sdk_lightsail.types.key_pair.deserialize_aws_json_1_1(
            data["keyPair"]
        )
    if "publicKeyBase64" in data:
        out["public_key_base64"] = data["publicKeyBase64"]
    if "privateKeyBase64" in data:
        out["private_key_base64"] = data["privateKeyBase64"]
    if "operation" in data:
        import aws_sdk_lightsail.types.operation

        out["operation"] = aws_sdk_lightsail.types.operation.deserialize_aws_json_1_1(
            data["operation"]
        )
    return out
