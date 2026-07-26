"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class DeleteKeyPairRequest(TypedDict, closed=True):
    key_pair_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the key pair to delete.</p>"""
    expected_fingerprint: NotRequired["capo_lightsail.types.string.string"]
    """<p>The RSA fingerprint of the Lightsail default key pair to delete.</p> <note> <p>The <code>expectedFingerprint</code> parameter is required only when specifying to delete a Lightsail default key pair.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteKeyPairRequest) -> dict:
    out: dict = {}
    out["keyPairName"] = value["key_pair_name"]
    if "expected_fingerprint" in value:
        out["expectedFingerprint"] = value["expected_fingerprint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteKeyPairRequest:
    out: DeleteKeyPairRequest = {}  # type: ignore[typeddict-item]
    if "keyPairName" in data:
        out["key_pair_name"] = data["keyPairName"]
    else:
        raise DeserializationError("DeleteKeyPairRequest.key_pair_name required")
    if "expectedFingerprint" in data:
        out["expected_fingerprint"] = data["expectedFingerprint"]
    return out
