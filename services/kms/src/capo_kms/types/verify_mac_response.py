"""Generated from Smithy shape ``com.amazonaws.kms#VerifyMacResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.boolean_type
    import capo_kms.types.key_id_type
    import capo_kms.types.mac_algorithm_spec


class VerifyMacResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The HMAC KMS key used in the verification.</p>"""
    mac_valid: "capo_kms.types.boolean_type.BooleanType"
    """<p>A Boolean value that indicates whether the HMAC was verified. A value of <code>True</code> indicates that the HMAC (<code>Mac</code>) was generated with the specified <code>Message</code>, HMAC KMS key (<code>KeyID</code>) and <code>MacAlgorithm.</code>.</p> <p>If the HMAC is not verified, the <code>VerifyMac</code> operation fails with a <code>KMSInvalidMacException</code> exception. This exception indicates that one or more of the inputs changed since the HMAC was computed.</p>"""
    mac_algorithm: NotRequired["capo_kms.types.mac_algorithm_spec.MacAlgorithmSpec"]
    """<p>The MAC algorithm used in the verification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyMacResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    out["MacValid"] = value.get("mac_valid", False)
    if "mac_algorithm" in value:
        import capo_kms.types.mac_algorithm_spec

        out["MacAlgorithm"] = capo_kms.types.mac_algorithm_spec.serialize_aws_json_1_1(
            value["mac_algorithm"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyMacResponse:
    out: VerifyMacResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "MacValid" in data:
        out["mac_valid"] = data["MacValid"]
    else:
        out["mac_valid"] = False
    if "MacAlgorithm" in data:
        import capo_kms.types.mac_algorithm_spec

        out["mac_algorithm"] = (
            capo_kms.types.mac_algorithm_spec.deserialize_aws_json_1_1(
                data["MacAlgorithm"]
            )
        )
    return out
