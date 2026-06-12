"""Generated from Smithy shape ``com.amazonaws.lightsail#GetKeyPairResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.key_pair


class GetKeyPairResult(TypedDict):
    key_pair: NotRequired["aws_sdk_lightsail.types.key_pair.KeyPair"]
    """<p>An array of key-value pairs containing information about the key pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPairResult) -> dict:
    out: dict = {}
    if "key_pair" in value:
        import aws_sdk_lightsail.types.key_pair

        out["keyPair"] = aws_sdk_lightsail.types.key_pair.serialize_aws_json_1_1(
            value["key_pair"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPairResult:
    out: GetKeyPairResult = {}  # type: ignore[typeddict-item]
    if "keyPair" in data:
        import aws_sdk_lightsail.types.key_pair

        out["key_pair"] = aws_sdk_lightsail.types.key_pair.deserialize_aws_json_1_1(
            data["keyPair"]
        )
    return out
