"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_string_list_value
    import capo_qbusiness.types.document_attribute_string_value
    import capo_qbusiness.types.long
    import capo_qbusiness.types.timestamp


class _DocumentAttributeValue_stringValue(TypedDict, closed=True):
    stringValue: "capo_qbusiness.types.document_attribute_string_value.DocumentAttributeStringValue"


class _DocumentAttributeValue_stringListValue(TypedDict, closed=True):
    stringListValue: "capo_qbusiness.types.document_attribute_string_list_value.DocumentAttributeStringListValue"


class _DocumentAttributeValue_longValue(TypedDict, closed=True):
    longValue: "capo_qbusiness.types.long.Long"


class _DocumentAttributeValue_dateValue(TypedDict, closed=True):
    dateValue: "capo_qbusiness.types.timestamp.Timestamp"


DocumentAttributeValue: TypeAlias = (
    _DocumentAttributeValue_stringValue
    | _DocumentAttributeValue_stringListValue
    | _DocumentAttributeValue_longValue
    | _DocumentAttributeValue_dateValue
)


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "stringListValue" in value:
        import capo_qbusiness.types.document_attribute_string_list_value

        return {
            "stringListValue": capo_qbusiness.types.document_attribute_string_list_value.serialize_json(
                value["stringListValue"]
            )
        }
    elif "longValue" in value:
        return {"longValue": value["longValue"]}
    elif "dateValue" in value:
        import capo_qbusiness.types.timestamp

        return {
            "dateValue": capo_qbusiness.types.timestamp.serialize_json(
                value["dateValue"]
            )
        }
    else:
        raise SerializationError("DocumentAttributeValue: no variant present")


def deserialize_json(data: dict) -> DocumentAttributeValue:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "stringListValue" in data:
        import capo_qbusiness.types.document_attribute_string_list_value

        return {
            "stringListValue": capo_qbusiness.types.document_attribute_string_list_value.deserialize_json(
                data["stringListValue"]
            )
        }
    elif "longValue" in data:
        return {"longValue": data["longValue"]}
    elif "dateValue" in data:
        import capo_qbusiness.types.timestamp

        return {
            "dateValue": capo_qbusiness.types.timestamp.deserialize_json(
                data["dateValue"]
            )
        }
    else:
        raise DeserializationError("DocumentAttributeValue: no recognized variant key")
