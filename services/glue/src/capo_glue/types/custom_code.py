"""Generated from Smithy shape ``com.amazonaws.glue#CustomCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.extended_string
    import capo_glue.types.glue_schemas
    import capo_glue.types.many_inputs
    import capo_glue.types.node_name


class CustomCode(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.many_inputs.ManyInputs"
    """<p>The data inputs identified by their node names.</p>"""
    code: "capo_glue.types.extended_string.ExtendedString"
    """<p>The custom code that is used to perform the data transformation.</p>"""
    class_name: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name defined for the custom code node class.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the custom code transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomCode) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.many_inputs

    out["Inputs"] = capo_glue.types.many_inputs.serialize_aws_json_1_1(value["inputs"])
    out["Code"] = value["code"]
    out["ClassName"] = value["class_name"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomCode:
    out: CustomCode = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomCode.name required")
    if "Inputs" in data:
        import capo_glue.types.many_inputs

        out["inputs"] = capo_glue.types.many_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("CustomCode.inputs required")
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("CustomCode.code required")
    if "ClassName" in data:
        out["class_name"] = data["ClassName"]
    else:
        raise DeserializationError("CustomCode.class_name required")
    if "OutputSchemas" in data:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
