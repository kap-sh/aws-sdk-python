"""Generated from Smithy shape ``com.amazonaws.lightsail#GetKeyPairResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.key_pair


class GetKeyPairResult(TypedDict, closed=True):
    key_pair: NotRequired["capo_lightsail.types.key_pair.KeyPair"]
    """<p>An array of key-value pairs containing information about the key pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPairResult) -> dict:
    out: dict = {}
    if "key_pair" in value:
        import capo_lightsail.types.key_pair

        out["keyPair"] = capo_lightsail.types.key_pair.serialize_aws_json_1_1(
            value["key_pair"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPairResult:
    out: GetKeyPairResult = {}  # type: ignore[typeddict-item]
    if "keyPair" in data:
        import capo_lightsail.types.key_pair

        out["key_pair"] = capo_lightsail.types.key_pair.deserialize_aws_json_1_1(
            data["keyPair"]
        )
    return out
