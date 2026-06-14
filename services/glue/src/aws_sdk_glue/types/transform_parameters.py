"""Generated from Smithy shape ``com.amazonaws.glue#TransformParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.find_matches_parameters
    import aws_sdk_glue.types.transform_type


class TransformParameters(TypedDict):
    transform_type: "aws_sdk_glue.types.transform_type.TransformType"
    r"""<p>The type of machine learning transform.</p> <p>For information about the types of machine learning transforms, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html\">Creating Machine Learning Transforms</a>.</p>"""
    find_matches_parameters: NotRequired[
        "aws_sdk_glue.types.find_matches_parameters.FindMatchesParameters"
    ]
    """<p>The parameters for the find matches algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformParameters) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.transform_type

    out["TransformType"] = aws_sdk_glue.types.transform_type.serialize_aws_json_1_1(
        value["transform_type"]
    )
    if "find_matches_parameters" in value:
        import aws_sdk_glue.types.find_matches_parameters

        out["FindMatchesParameters"] = (
            aws_sdk_glue.types.find_matches_parameters.serialize_aws_json_1_1(
                value["find_matches_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformParameters:
    out: TransformParameters = {}  # type: ignore[typeddict-item]
    if "TransformType" in data:
        import aws_sdk_glue.types.transform_type

        out["transform_type"] = (
            aws_sdk_glue.types.transform_type.deserialize_aws_json_1_1(
                data["TransformType"]
            )
        )
    else:
        raise DeserializationError("TransformParameters.transform_type required")
    if "FindMatchesParameters" in data:
        import aws_sdk_glue.types.find_matches_parameters

        out["find_matches_parameters"] = (
            aws_sdk_glue.types.find_matches_parameters.deserialize_aws_json_1_1(
                data["FindMatchesParameters"]
            )
        )
    return out
