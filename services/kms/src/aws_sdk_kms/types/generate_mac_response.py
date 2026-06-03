"""Generated from Smithy shape ``com.amazonaws.kms#GenerateMacResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.ciphertext_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.mac_algorithm_spec


class GenerateMacResponse(TypedDict):
    mac: NotRequired["aws_sdk_kms.types.ciphertext_type.CiphertextType"]
    """<p>The hash-based message authentication code (HMAC) that was generated for the specified message, HMAC KMS key, and MAC algorithm.</p> <p>This is the standard, raw HMAC defined in <a href=\"https://datatracker.ietf.org/doc/html/rfc2104\">RFC 2104</a>.</p>"""
    mac_algorithm: NotRequired["aws_sdk_kms.types.mac_algorithm_spec.MacAlgorithmSpec"]
    """<p>The MAC algorithm that was used to generate the HMAC.</p>"""
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The HMAC KMS key used in the operation.</p>"""
