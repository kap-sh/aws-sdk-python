"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfKmsKeysToGrant``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.kms_key_to_grant

ListOfKmsKeysToGrant: TypeAlias = list[
    "capo_dataexchange.types.kms_key_to_grant.KmsKeyToGrant"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfKmsKeysToGrant) -> list:
    import capo_dataexchange.types.kms_key_to_grant

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.kms_key_to_grant.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfKmsKeysToGrant:
    import capo_dataexchange.types.kms_key_to_grant

    out: ListOfKmsKeysToGrant = []
    for item in data:
        out.append(capo_dataexchange.types.kms_key_to_grant.deserialize_json(item))
    return out
