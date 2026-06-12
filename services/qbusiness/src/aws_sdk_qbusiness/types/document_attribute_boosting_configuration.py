"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.date_attribute_boosting_configuration
    import aws_sdk_qbusiness.types.number_attribute_boosting_configuration
    import aws_sdk_qbusiness.types.string_attribute_boosting_configuration
    import aws_sdk_qbusiness.types.string_list_attribute_boosting_configuration

class _DocumentAttributeBoostingConfiguration_numberConfiguration(TypedDict):
    numberConfiguration: "aws_sdk_qbusiness.types.number_attribute_boosting_configuration.NumberAttributeBoostingConfiguration"


class _DocumentAttributeBoostingConfiguration_stringConfiguration(TypedDict):
    stringConfiguration: "aws_sdk_qbusiness.types.string_attribute_boosting_configuration.StringAttributeBoostingConfiguration"


class _DocumentAttributeBoostingConfiguration_dateConfiguration(TypedDict):
    dateConfiguration: "aws_sdk_qbusiness.types.date_attribute_boosting_configuration.DateAttributeBoostingConfiguration"


class _DocumentAttributeBoostingConfiguration_stringListConfiguration(TypedDict):
    stringListConfiguration: "aws_sdk_qbusiness.types.string_list_attribute_boosting_configuration.StringListAttributeBoostingConfiguration"

DocumentAttributeBoostingConfiguration: TypeAlias = _DocumentAttributeBoostingConfiguration_numberConfiguration | _DocumentAttributeBoostingConfiguration_stringConfiguration | _DocumentAttributeBoostingConfiguration_dateConfiguration | _DocumentAttributeBoostingConfiguration_stringListConfiguration

# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeBoostingConfiguration) -> dict:
    if "numberConfiguration" in value:
        import aws_sdk_qbusiness.types.number_attribute_boosting_configuration
        return {"numberConfiguration": aws_sdk_qbusiness.types.number_attribute_boosting_configuration.serialize_json(value["numberConfiguration"])}
    elif "stringConfiguration" in value:
        import aws_sdk_qbusiness.types.string_attribute_boosting_configuration
        return {"stringConfiguration": aws_sdk_qbusiness.types.string_attribute_boosting_configuration.serialize_json(value["stringConfiguration"])}
    elif "dateConfiguration" in value:
        import aws_sdk_qbusiness.types.date_attribute_boosting_configuration
        return {"dateConfiguration": aws_sdk_qbusiness.types.date_attribute_boosting_configuration.serialize_json(value["dateConfiguration"])}
    elif "stringListConfiguration" in value:
        import aws_sdk_qbusiness.types.string_list_attribute_boosting_configuration
        return {"stringListConfiguration": aws_sdk_qbusiness.types.string_list_attribute_boosting_configuration.serialize_json(value["stringListConfiguration"])}
    else:
        raise SerializationError("DocumentAttributeBoostingConfiguration: no variant present")


def deserialize_json(data: dict) -> DocumentAttributeBoostingConfiguration:
    if "numberConfiguration" in data:
        import aws_sdk_qbusiness.types.number_attribute_boosting_configuration
        return {"numberConfiguration": aws_sdk_qbusiness.types.number_attribute_boosting_configuration.deserialize_json(data["numberConfiguration"])}
    elif "stringConfiguration" in data:
        import aws_sdk_qbusiness.types.string_attribute_boosting_configuration
        return {"stringConfiguration": aws_sdk_qbusiness.types.string_attribute_boosting_configuration.deserialize_json(data["stringConfiguration"])}
    elif "dateConfiguration" in data:
        import aws_sdk_qbusiness.types.date_attribute_boosting_configuration
        return {"dateConfiguration": aws_sdk_qbusiness.types.date_attribute_boosting_configuration.deserialize_json(data["dateConfiguration"])}
    elif "stringListConfiguration" in data:
        import aws_sdk_qbusiness.types.string_list_attribute_boosting_configuration
        return {"stringListConfiguration": aws_sdk_qbusiness.types.string_list_attribute_boosting_configuration.deserialize_json(data["stringListConfiguration"])}
    else:
        raise DeserializationError("DocumentAttributeBoostingConfiguration: no recognized variant key")