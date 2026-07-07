"""Generated from Smithy shape ``com.amazonaws.glue#Spigot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.prob
    import aws_sdk_glue.types.topk


class Spigot(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    path: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>A path in Amazon S3 where the transform will write a subset of records from the dataset to a JSON file in an Amazon S3 bucket.</p>"""
    topk: NotRequired["aws_sdk_glue.types.topk.Topk"]
    """<p>Specifies a number of records to write starting from the beginning of the dataset.</p>"""
    prob: NotRequired["aws_sdk_glue.types.prob.Prob"]
    """<p>The probability (a decimal value with a maximum value of 1) of picking any given record. A value of 1 indicates that each row read from the dataset should be included in the sample output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Spigot) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Path"] = value["path"]
    if "topk" in value:
        out["Topk"] = value["topk"]
    if "prob" in value:
        out["Prob"] = value["prob"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Spigot:
    out: Spigot = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Spigot.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Spigot.inputs required")
    if "Path" in data:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("Spigot.path required")
    if "Topk" in data:
        out["topk"] = data["Topk"]
    if "Prob" in data:
        out["prob"] = data["Prob"]
    return out
