"""Generated from Smithy shape ``com.amazonaws.neptunedata#CustomModelTransformParameters``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_neptunedata.errors import DeserializationError

class CustomModelTransformParameters(TypedDict):
    source_s3_directory_path: "str"
    """<p>The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a <code>model-hpo-configuration.json</code> file.</p>"""
    transform_entry_point_script: NotRequired["str"]
    """<p>The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments. The default is <code>transform.py</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CustomModelTransformParameters) -> dict:
    out: dict = {}
    out["sourceS3DirectoryPath"] = value["source_s3_directory_path"]
    if "transform_entry_point_script" in value:
        out["transformEntryPointScript"] = value["transform_entry_point_script"]
    return out


def deserialize_json(data: dict) -> CustomModelTransformParameters:
    out: CustomModelTransformParameters = {}  # type: ignore[typeddict-item]
    if "sourceS3DirectoryPath" in data:
        out["source_s3_directory_path"] = data["sourceS3DirectoryPath"]
    else:
        raise DeserializationError("CustomModelTransformParameters.source_s3_directory_path required")
    if "transformEntryPointScript" in data:
        out["transform_entry_point_script"] = data["transformEntryPointScript"]
    return out