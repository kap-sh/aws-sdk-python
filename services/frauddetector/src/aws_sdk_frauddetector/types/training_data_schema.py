"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingDataSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.label_schema
    import aws_sdk_frauddetector.types.list_of_strings


class TrainingDataSchema(TypedDict, closed=True):
    model_variables: "aws_sdk_frauddetector.types.list_of_strings.ListOfStrings"
    """<p>The training data schema variables.</p>"""
    label_schema: NotRequired["aws_sdk_frauddetector.types.label_schema.LabelSchema"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingDataSchema) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.list_of_strings

    out["modelVariables"] = (
        aws_sdk_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["model_variables"]
        )
    )
    if "label_schema" in value:
        import aws_sdk_frauddetector.types.label_schema

        out["labelSchema"] = (
            aws_sdk_frauddetector.types.label_schema.serialize_aws_json_1_1(
                value["label_schema"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingDataSchema:
    out: TrainingDataSchema = {}  # type: ignore[typeddict-item]
    if "modelVariables" in data:
        import aws_sdk_frauddetector.types.list_of_strings

        out["model_variables"] = (
            aws_sdk_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["modelVariables"]
            )
        )
    else:
        raise DeserializationError("TrainingDataSchema.model_variables required")
    if "labelSchema" in data:
        import aws_sdk_frauddetector.types.label_schema

        out["label_schema"] = (
            aws_sdk_frauddetector.types.label_schema.deserialize_aws_json_1_1(
                data["labelSchema"]
            )
        )
    return out
