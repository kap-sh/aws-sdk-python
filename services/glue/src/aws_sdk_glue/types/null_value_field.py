"""Generated from Smithy shape ``com.amazonaws.glue#NullValueField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.datatype
    import aws_sdk_glue.types.enclosed_in_string_property


class NullValueField(TypedDict, closed=True):
    value: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The value of the null placeholder.</p>"""
    datatype: "aws_sdk_glue.types.datatype.Datatype"
    """<p>The datatype of the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NullValueField) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import aws_sdk_glue.types.datatype

    out["Datatype"] = aws_sdk_glue.types.datatype.serialize_aws_json_1_1(
        value["datatype"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NullValueField:
    out: NullValueField = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("NullValueField.value required")
    if "Datatype" in data:
        import aws_sdk_glue.types.datatype

        out["datatype"] = aws_sdk_glue.types.datatype.deserialize_aws_json_1_1(
            data["Datatype"]
        )
    else:
        raise DeserializationError("NullValueField.datatype required")
    return out
