"""Generated from Smithy shape ``com.amazonaws.groundstation#KmsKey``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_groundstation.types.key_alias_arn
    import capo_groundstation.types.key_alias_name
    import capo_groundstation.types.key_arn


class _KmsKey_kmsKeyArn(TypedDict, closed=True):
    kmsKeyArn: "capo_groundstation.types.key_arn.KeyArn"


class _KmsKey_kmsAliasArn(TypedDict, closed=True):
    kmsAliasArn: "capo_groundstation.types.key_alias_arn.KeyAliasArn"


class _KmsKey_kmsAliasName(TypedDict, closed=True):
    kmsAliasName: "capo_groundstation.types.key_alias_name.KeyAliasName"


KmsKey: TypeAlias = _KmsKey_kmsKeyArn | _KmsKey_kmsAliasArn | _KmsKey_kmsAliasName


# --- restJson1 ser/de ---
def serialize_json(value: KmsKey) -> dict:
    if "kmsKeyArn" in value:
        return {"kmsKeyArn": value["kmsKeyArn"]}
    elif "kmsAliasArn" in value:
        return {"kmsAliasArn": value["kmsAliasArn"]}
    elif "kmsAliasName" in value:
        return {"kmsAliasName": value["kmsAliasName"]}
    else:
        raise SerializationError("KmsKey: no variant present")


def deserialize_json(data: dict) -> KmsKey:
    if "kmsKeyArn" in data:
        return {"kmsKeyArn": data["kmsKeyArn"]}
    elif "kmsAliasArn" in data:
        return {"kmsAliasArn": data["kmsAliasArn"]}
    elif "kmsAliasName" in data:
        return {"kmsAliasName": data["kmsAliasName"]}
    else:
        raise DeserializationError("KmsKey: no recognized variant key")
