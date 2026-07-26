"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingOverrideMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_boosting_configuration
    import capo_qbusiness.types.document_attribute_key

DocumentAttributeBoostingOverrideMap: TypeAlias = dict[
    "capo_qbusiness.types.document_attribute_key.DocumentAttributeKey",
    "capo_qbusiness.types.document_attribute_boosting_configuration.DocumentAttributeBoostingConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentAttributeBoostingOverrideMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_qbusiness.types.document_attribute_boosting_configuration

        out[key] = (
            capo_qbusiness.types.document_attribute_boosting_configuration.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentAttributeBoostingOverrideMap:
    out: DocumentAttributeBoostingOverrideMap = {}
    for key, value in data.items():
        import capo_qbusiness.types.document_attribute_boosting_configuration

        out[key] = (
            capo_qbusiness.types.document_attribute_boosting_configuration.deserialize_json(
                value
            )
        )
    return out
