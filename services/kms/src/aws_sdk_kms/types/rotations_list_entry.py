"""Generated from Smithy shape ``com.amazonaws.kms#RotationsListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.backing_key_id_type
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.expiration_model_type
    import aws_sdk_kms.types.import_state
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.key_material_description_type
    import aws_sdk_kms.types.key_material_state
    import aws_sdk_kms.types.rotation_type


class RotationsListEntry(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Unique identifier of the key.</p>"""
    key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>Unique identifier of the key material. </p>"""
    key_material_description: NotRequired[
        "aws_sdk_kms.types.key_material_description_type.KeyMaterialDescriptionType"
    ]
    """<p>User-specified description of the key material. This field is only present for symmetric encryption KMS keys with <code>EXTERNAL</code> origin.</p>"""
    import_state: NotRequired["aws_sdk_kms.types.import_state.ImportState"]
    """<p>Indicates if the key material is currently imported into KMS. It has two possible values: <code>IMPORTED</code> or <code>PENDING_IMPORT</code>. This field is only present for symmetric encryption KMS keys with <code>EXTERNAL</code> origin.</p>"""
    key_material_state: NotRequired[
        "aws_sdk_kms.types.key_material_state.KeyMaterialState"
    ]
    """<p>There are four possible values for this field: <code>CURRENT</code>, <code>NON_CURRENT</code>, <code>PENDING_MULTI_REGION_IMPORT_AND_ROTATION</code> and <code>PENDING_ROTATION</code>. KMS uses <code>CURRENT</code> key material for both encryption and decryption and <code>NON_CURRENT</code> key material only for decryption. <code>PENDING_ROTATION</code> identifies key material that has been imported for on-demand key rotation but the rotation hasn't completed. The key material state <code>PENDING_MULTI_REGION_IMPORT_AND_ROTATION</code> is unique to multi-region, symmetric encryption keys with imported key material. It indicates key material that has been imported into the primary Region key but not all of the replica Region keys. When this key material is imported in to all of the replica Region keys, the key material state will change to <code>PENDING_ROTATION</code>. Key material in <code>PENDING_MULTI_REGION_IMPORT_AND_ROTATION</code> or <code>PENDING_ROTATION</code> state is not permanently associated with the KMS key. You can delete this key material and import different key material in its place. The <code>PENDING_MULTI_REGION_IMPORT_AND_ROTATION</code> and <code>PENDING_ROTATION</code> values are only used in symmetric encryption keys with imported key material. The other values, <code>CURRENT</code> and <code>NON_CURRENT</code>, are used for all KMS keys that support automatic or on-demand key rotation.</p>"""
    expiration_model: NotRequired[
        "aws_sdk_kms.types.expiration_model_type.ExpirationModelType"
    ]
    """<p>Indicates if the key material is configured to automatically expire. There are two possible values for this field: <code>KEY_MATERIAL_EXPIRES</code> and <code>KEY_MATERIAL_DOES_NOT_EXPIRE</code>. For any key material that expires, the expiration date and time is indicated in <code>ValidTo</code>. This field is only present for symmetric encryption KMS keys with <code>EXTERNAL</code> origin.</p>"""
    valid_to: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>Date and time at which the key material expires. This field is only present for symmetric encryption KMS keys with <code>EXTERNAL</code> origin in rotation list entries with an <code>ExpirationModel</code> value of <code>KEY_MATERIAL_EXPIRES</code>.</p>"""
    rotation_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>Date and time that the key material rotation completed. Formatted as Unix time. This field is not present for the first key material or an imported key material in <code>PENDING_ROTATION</code> state.</p>"""
    rotation_type: NotRequired["aws_sdk_kms.types.rotation_type.RotationType"]
    """<p>Identifies whether the key material rotation was a scheduled <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable-disable.html\">automatic rotation</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-on-demand.html\">on-demand rotation</a>. This field is not present for the first key material or an imported key material in <code>PENDING_ROTATION</code> state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationsListEntry) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    if "key_material_description" in value:
        out["KeyMaterialDescription"] = value["key_material_description"]
    if "import_state" in value:
        import aws_sdk_kms.types.import_state

        out["ImportState"] = aws_sdk_kms.types.import_state.serialize_aws_json_1_1(
            value["import_state"]
        )
    if "key_material_state" in value:
        import aws_sdk_kms.types.key_material_state

        out["KeyMaterialState"] = (
            aws_sdk_kms.types.key_material_state.serialize_aws_json_1_1(
                value["key_material_state"]
            )
        )
    if "expiration_model" in value:
        import aws_sdk_kms.types.expiration_model_type

        out["ExpirationModel"] = (
            aws_sdk_kms.types.expiration_model_type.serialize_aws_json_1_1(
                value["expiration_model"]
            )
        )
    if "valid_to" in value:
        import aws_sdk_kms.types.date_type

        out["ValidTo"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["valid_to"]
        )
    if "rotation_date" in value:
        import aws_sdk_kms.types.date_type

        out["RotationDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["rotation_date"]
        )
    if "rotation_type" in value:
        import aws_sdk_kms.types.rotation_type

        out["RotationType"] = aws_sdk_kms.types.rotation_type.serialize_aws_json_1_1(
            value["rotation_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotationsListEntry:
    out: RotationsListEntry = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyMaterialId" in data:
        out["key_material_id"] = data["KeyMaterialId"]
    if "KeyMaterialDescription" in data:
        out["key_material_description"] = data["KeyMaterialDescription"]
    if "ImportState" in data:
        import aws_sdk_kms.types.import_state

        out["import_state"] = aws_sdk_kms.types.import_state.deserialize_aws_json_1_1(
            data["ImportState"]
        )
    if "KeyMaterialState" in data:
        import aws_sdk_kms.types.key_material_state

        out["key_material_state"] = (
            aws_sdk_kms.types.key_material_state.deserialize_aws_json_1_1(
                data["KeyMaterialState"]
            )
        )
    if "ExpirationModel" in data:
        import aws_sdk_kms.types.expiration_model_type

        out["expiration_model"] = (
            aws_sdk_kms.types.expiration_model_type.deserialize_aws_json_1_1(
                data["ExpirationModel"]
            )
        )
    if "ValidTo" in data:
        import aws_sdk_kms.types.date_type

        out["valid_to"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["ValidTo"]
        )
    if "RotationDate" in data:
        import aws_sdk_kms.types.date_type

        out["rotation_date"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["RotationDate"]
        )
    if "RotationType" in data:
        import aws_sdk_kms.types.rotation_type

        out["rotation_type"] = aws_sdk_kms.types.rotation_type.deserialize_aws_json_1_1(
            data["RotationType"]
        )
    return out
