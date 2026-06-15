"""Generated from Smithy shape ``com.amazonaws.kms#ImportKeyMaterialResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.backing_key_id_type
    import aws_sdk_kms.types.key_id_type


class ImportKeyMaterialResponse(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key into which key material was imported.</p>"""
    key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>Identifies the imported key material.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportKeyMaterialResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportKeyMaterialResponse:
    out: ImportKeyMaterialResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyMaterialId" in data:
        out["key_material_id"] = data["KeyMaterialId"]
    return out
