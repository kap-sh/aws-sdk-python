"""Generated from Smithy shape ``com.amazonaws.glue#Aggregate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.aggregate_operations
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class Aggregate(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>Specifies the fields and rows to use as inputs for the aggregate transform.</p>"""
    groups: "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    """<p>Specifies the fields to group by.</p>"""
    aggs: "aws_sdk_glue.types.aggregate_operations.AggregateOperations"
    """<p>Specifies the aggregate functions to be performed on specified fields. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Aggregate) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import aws_sdk_glue.types.glue_studio_path_list

    out["Groups"] = aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["groups"]
    )
    import aws_sdk_glue.types.aggregate_operations

    out["Aggs"] = aws_sdk_glue.types.aggregate_operations.serialize_aws_json_1_1(
        value["aggs"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Aggregate:
    out: Aggregate = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Aggregate.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Aggregate.inputs required")
    if "Groups" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["groups"] = (
            aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    else:
        raise DeserializationError("Aggregate.groups required")
    if "Aggs" in data:
        import aws_sdk_glue.types.aggregate_operations

        out["aggs"] = aws_sdk_glue.types.aggregate_operations.deserialize_aws_json_1_1(
            data["Aggs"]
        )
    else:
        raise DeserializationError("Aggregate.aggs required")
    return out
