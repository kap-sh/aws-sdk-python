"""Generated from Smithy shape ``com.amazonaws.kms#VerifyMacResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.boolean_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.mac_algorithm_spec


class VerifyMacResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The HMAC KMS key used in the verification.</p>"""
    mac_valid: "awd_sdk_kms.types.boolean_type.BooleanType"
    """<p>A Boolean value that indicates whether the HMAC was verified. A value of <code>True</code> indicates that the HMAC (<code>Mac</code>) was generated with the specified <code>Message</code>, HMAC KMS key (<code>KeyID</code>) and <code>MacAlgorithm.</code>.</p> <p>If the HMAC is not verified, the <code>VerifyMac</code> operation fails with a <code>KMSInvalidMacException</code> exception. This exception indicates that one or more of the inputs changed since the HMAC was computed.</p>"""
    mac_algorithm: NotRequired["awd_sdk_kms.types.mac_algorithm_spec.MacAlgorithmSpec"]
    """<p>The MAC algorithm used in the verification.</p>"""
