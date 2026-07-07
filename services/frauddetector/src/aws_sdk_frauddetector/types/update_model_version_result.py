"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateModelVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float_version_string
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum
    import aws_sdk_frauddetector.types.string


class UpdateModelVersionResult(TypedDict, closed=True):
    model_id: NotRequired[
        "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    ]
    """<p>The model ID.</p>"""
    model_type: NotRequired["aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"]
    """<p>The model type.</p>"""
    model_version_number: NotRequired[
        "aws_sdk_frauddetector.types.float_version_string.floatVersionString"
    ]
    """<p>The model version number of the model version updated.</p>"""
    status: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The status of the updated model version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateModelVersionResult) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "model_type" in value:
        import aws_sdk_frauddetector.types.model_type_enum

        out["modelType"] = (
            aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
                value["model_type"]
            )
        )
    if "model_version_number" in value:
        out["modelVersionNumber"] = value["model_version_number"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateModelVersionResult:
    out: UpdateModelVersionResult = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    if "status" in data:
        out["status"] = data["status"]
    return out
