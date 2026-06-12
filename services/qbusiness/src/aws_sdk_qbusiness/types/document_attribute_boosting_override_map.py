"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingOverrideMap``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_attribute_key
    import aws_sdk_qbusiness.types.document_attribute_boosting_configuration

DocumentAttributeBoostingOverrideMap: TypeAlias = dict["aws_sdk_qbusiness.types.document_attribute_key.DocumentAttributeKey", "aws_sdk_qbusiness.types.document_attribute_boosting_configuration.DocumentAttributeBoostingConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentAttributeBoostingOverrideMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_qbusiness.types.document_attribute_boosting_configuration
        out[key] = aws_sdk_qbusiness.types.document_attribute_boosting_configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DocumentAttributeBoostingOverrideMap:
    out: DocumentAttributeBoostingOverrideMap = {}
    for key, value in data.items():
        import aws_sdk_qbusiness.types.document_attribute_boosting_configuration
        out[key] = aws_sdk_qbusiness.types.document_attribute_boosting_configuration.deserialize_json(value)
    return out