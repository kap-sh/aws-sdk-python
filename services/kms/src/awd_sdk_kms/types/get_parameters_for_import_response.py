"""Generated from Smithy shape ``com.amazonaws.kms#GetParametersForImportResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.ciphertext_type
    import awd_sdk_kms.types.date_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.plaintext_type


class GetParametersForImportResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key to use in a subsequent <a>ImportKeyMaterial</a> request. This is the same KMS key specified in the <code>GetParametersForImport</code> request.</p>"""
    import_token: NotRequired["awd_sdk_kms.types.ciphertext_type.CiphertextType"]
    """<p>The import token to send in a subsequent <a>ImportKeyMaterial</a> request.</p>"""
    public_key: NotRequired["awd_sdk_kms.types.plaintext_type.PlaintextType"]
    """<p>The public key to use to encrypt the key material before importing it with <a>ImportKeyMaterial</a>.</p>"""
    parameters_valid_to: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an <a>ImportKeyMaterial</a> request and you must send another <code>GetParametersForImport</code> request to get new ones.</p>"""
