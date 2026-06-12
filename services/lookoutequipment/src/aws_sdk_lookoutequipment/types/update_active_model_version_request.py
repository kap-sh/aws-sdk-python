"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateActiveModelVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_version


class UpdateActiveModelVersionRequest(TypedDict):
    model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the machine learning model for which the active model version is being set.</p>"""
    model_version: "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    """<p>The version of the machine learning model for which the active model version is being set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateActiveModelVersionRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateActiveModelVersionRequest:
    out: UpdateActiveModelVersionRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError(
            "UpdateActiveModelVersionRequest.model_name required"
        )
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    else:
        raise DeserializationError(
            "UpdateActiveModelVersionRequest.model_version required"
        )
    return out
