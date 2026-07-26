"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EncryptionState``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.kms_encryption_state


class _EncryptionState_kmsEncryptionState(TypedDict, closed=True):
    kmsEncryptionState: (
        "capo_verifiedpermissions.types.kms_encryption_state.KmsEncryptionState"
    )


class _EncryptionState_default(TypedDict, closed=True):
    default: "None"


EncryptionState: TypeAlias = (
    _EncryptionState_kmsEncryptionState | _EncryptionState_default
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionState) -> dict:
    if "kmsEncryptionState" in value:
        import capo_verifiedpermissions.types.kms_encryption_state

        return {
            "kmsEncryptionState": capo_verifiedpermissions.types.kms_encryption_state.serialize_aws_json_1_0(
                value["kmsEncryptionState"]
            )
        }
    elif "default" in value:
        return {"default": {}}
    else:
        raise SerializationError("EncryptionState: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionState:
    if "kmsEncryptionState" in data:
        import capo_verifiedpermissions.types.kms_encryption_state

        return {
            "kmsEncryptionState": capo_verifiedpermissions.types.kms_encryption_state.deserialize_aws_json_1_0(
                data["kmsEncryptionState"]
            )
        }
    elif "default" in data:
        return {"default": None}
    else:
        raise DeserializationError("EncryptionState: no recognized variant key")
