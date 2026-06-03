"""Generated from Smithy shape ``com.amazonaws.kms#ReEncryptResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.backing_key_id_type
    import awd_sdk_kms.types.ciphertext_type
    import awd_sdk_kms.types.encryption_algorithm_spec
    import awd_sdk_kms.types.key_id_type


class ReEncryptResponse(TypedDict):
    ciphertext_blob: NotRequired["awd_sdk_kms.types.ciphertext_type.CiphertextType"]
    """<p>The reencrypted data. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    source_key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Unique identifier of the KMS key used to originally encrypt the data.</p>"""
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key that was used to reencrypt the data.</p>"""
    source_encryption_algorithm: NotRequired[
        "awd_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to decrypt the ciphertext before it was reencrypted.</p>"""
    destination_encryption_algorithm: NotRequired[
        "awd_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to reencrypt the data.</p>"""
    source_key_material_id: NotRequired[
        "awd_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to originally encrypt the data. This field is present only when the original encryption used a symmetric encryption KMS key.</p>"""
    destination_key_material_id: NotRequired[
        "awd_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to reencrypt the data. This field is present only when data is reencrypted using a symmetric encryption KMS key.</p>"""
