"""Generated from Smithy shape ``com.amazonaws.kms#DeleteImportedKeyMaterialResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.backing_key_id_response_type
    import awd_sdk_kms.types.key_id_type


class DeleteImportedKeyMaterialResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key from which the key material was deleted.</p>"""
    key_material_id: NotRequired[
        "awd_sdk_kms.types.backing_key_id_response_type.BackingKeyIdResponseType"
    ]
    """<p>Identifies the deleted key material.</p>"""
