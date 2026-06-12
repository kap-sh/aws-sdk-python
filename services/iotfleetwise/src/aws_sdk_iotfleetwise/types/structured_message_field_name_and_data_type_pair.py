"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessageFieldNameAndDataTypePair``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.structure_message_name
    import aws_sdk_iotfleetwise.types.structured_message


class StructuredMessageFieldNameAndDataTypePair(TypedDict):
    field_name: "aws_sdk_iotfleetwise.types.structure_message_name.StructureMessageName"
    """<p>The field name of the structured message. It determines how a data value is referenced in the target language. </p>"""
    data_type: "aws_sdk_iotfleetwise.types.structured_message.StructuredMessage"
    """<p>The data type. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessageFieldNameAndDataTypePair) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    import aws_sdk_iotfleetwise.types.structured_message

    out["dataType"] = (
        aws_sdk_iotfleetwise.types.structured_message.serialize_aws_json_1_0(
            value["data_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StructuredMessageFieldNameAndDataTypePair:
    out: StructuredMessageFieldNameAndDataTypePair = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError(
            "StructuredMessageFieldNameAndDataTypePair.field_name required"
        )
    if "dataType" in data:
        import aws_sdk_iotfleetwise.types.structured_message

        out["data_type"] = (
            aws_sdk_iotfleetwise.types.structured_message.deserialize_aws_json_1_0(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError(
            "StructuredMessageFieldNameAndDataTypePair.data_type required"
        )
    return out
