"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ImportModelVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_version
    import aws_sdk_lookoutequipment.types.model_version_arn
    import aws_sdk_lookoutequipment.types.model_version_status


class ImportModelVersionResponse(TypedDict, closed=True):
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name for the machine learning model.</p>"""
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model being created. </p>"""
    model_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model version being created. </p>"""
    model_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The version of the model being created.</p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_status.ModelVersionStatus"
    ]
    """<p>The status of the <code>ImportModelVersion</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportModelVersionResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "model_version_arn" in value:
        out["ModelVersionArn"] = value["model_version_arn"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.model_version_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.model_version_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportModelVersionResponse:
    out: ImportModelVersionResponse = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "ModelVersionArn" in data:
        out["model_version_arn"] = data["ModelVersionArn"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.model_version_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.model_version_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
