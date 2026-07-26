"""Generated from Smithy shape ``com.amazonaws.glue#StartImportLabelsTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.replace_boolean
    import capo_glue.types.uri_string


class StartImportLabelsTaskRunRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    input_s3_path: "capo_glue.types.uri_string.UriString"
    """<p>The Amazon Simple Storage Service (Amazon S3) path from where you import the labels.</p>"""
    replace_all_labels: "capo_glue.types.replace_boolean.ReplaceBoolean"
    """<p>Indicates whether to overwrite your existing labels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportLabelsTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    out["InputS3Path"] = value["input_s3_path"]
    out["ReplaceAllLabels"] = value.get("replace_all_labels", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportLabelsTaskRunRequest:
    out: StartImportLabelsTaskRunRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError(
            "StartImportLabelsTaskRunRequest.transform_id required"
        )
    if "InputS3Path" in data:
        out["input_s3_path"] = data["InputS3Path"]
    else:
        raise DeserializationError(
            "StartImportLabelsTaskRunRequest.input_s3_path required"
        )
    if "ReplaceAllLabels" in data:
        out["replace_all_labels"] = data["ReplaceAllLabels"]
    else:
        out["replace_all_labels"] = False
    return out
