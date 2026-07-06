"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.field_name_string
    import aws_sdk_data_pipeline.types.parameter_attribute_list


class ParameterObject(TypedDict, closed=True):
    id: "aws_sdk_data_pipeline.types.field_name_string.fieldNameString"
    """<p>The ID of the parameter object. </p>"""
    attributes: (
        "aws_sdk_data_pipeline.types.parameter_attribute_list.ParameterAttributeList"
    )
    """<p>The attributes of the parameter object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterObject) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_data_pipeline.types.parameter_attribute_list

    out["attributes"] = (
        aws_sdk_data_pipeline.types.parameter_attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterObject:
    out: ParameterObject = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ParameterObject.id required")
    if "attributes" in data:
        import aws_sdk_data_pipeline.types.parameter_attribute_list

        out["attributes"] = (
            aws_sdk_data_pipeline.types.parameter_attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError("ParameterObject.attributes required")
    return out
