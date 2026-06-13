"""Generated from Smithy shape ``com.amazonaws.bedrock#GetInferenceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_arn
    import aws_sdk_bedrock.types.inference_profile_description
    import aws_sdk_bedrock.types.inference_profile_id
    import aws_sdk_bedrock.types.inference_profile_models
    import aws_sdk_bedrock.types.inference_profile_name
    import aws_sdk_bedrock.types.inference_profile_status
    import aws_sdk_bedrock.types.inference_profile_type
    import aws_sdk_bedrock.types.timestamp


class GetInferenceProfileResponse(TypedDict):
    inference_profile_name: (
        "aws_sdk_bedrock.types.inference_profile_name.InferenceProfileName"
    )
    """<p>The name of the inference profile.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.inference_profile_description.InferenceProfileDescription"
    ]
    """<p>The description of the inference profile.</p>"""
    created_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the inference profile was created.</p>"""
    updated_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the inference profile was last updated.</p>"""
    inference_profile_arn: (
        "aws_sdk_bedrock.types.inference_profile_arn.InferenceProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the inference profile.</p>"""
    models: "aws_sdk_bedrock.types.inference_profile_models.InferenceProfileModels"
    """<p>A list of information about each model in the inference profile.</p>"""
    inference_profile_id: (
        "aws_sdk_bedrock.types.inference_profile_id.InferenceProfileId"
    )
    """<p>The unique identifier of the inference profile.</p>"""
    status: "aws_sdk_bedrock.types.inference_profile_status.InferenceProfileStatus"
    """<p>The status of the inference profile. <code>ACTIVE</code> means that the inference profile is ready to be used.</p>"""
    type: "aws_sdk_bedrock.types.inference_profile_type.InferenceProfileType"
    """<p>The type of the inference profile. The following types are possible:</p> <ul> <li> <p> <code>SYSTEM_DEFINED</code> – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.</p> </li> <li> <p> <code>APPLICATION</code> – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInferenceProfileResponse) -> dict:
    out: dict = {}
    out["inferenceProfileName"] = value["inference_profile_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    out["inferenceProfileArn"] = value["inference_profile_arn"]
    import aws_sdk_bedrock.types.inference_profile_models

    out["models"] = aws_sdk_bedrock.types.inference_profile_models.serialize_json(
        value["models"]
    )
    out["inferenceProfileId"] = value["inference_profile_id"]
    import aws_sdk_bedrock.types.inference_profile_status

    out["status"] = aws_sdk_bedrock.types.inference_profile_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock.types.inference_profile_type

    out["type"] = aws_sdk_bedrock.types.inference_profile_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> GetInferenceProfileResponse:
    out: GetInferenceProfileResponse = {}  # type: ignore[typeddict-item]
    if "inferenceProfileName" in data:
        out["inference_profile_name"] = data["inferenceProfileName"]
    else:
        raise DeserializationError(
            "GetInferenceProfileResponse.inference_profile_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "inferenceProfileArn" in data:
        out["inference_profile_arn"] = data["inferenceProfileArn"]
    else:
        raise DeserializationError(
            "GetInferenceProfileResponse.inference_profile_arn required"
        )
    if "models" in data:
        import aws_sdk_bedrock.types.inference_profile_models

        out["models"] = aws_sdk_bedrock.types.inference_profile_models.deserialize_json(
            data["models"]
        )
    else:
        raise DeserializationError("GetInferenceProfileResponse.models required")
    if "inferenceProfileId" in data:
        out["inference_profile_id"] = data["inferenceProfileId"]
    else:
        raise DeserializationError(
            "GetInferenceProfileResponse.inference_profile_id required"
        )
    if "status" in data:
        import aws_sdk_bedrock.types.inference_profile_status

        out["status"] = aws_sdk_bedrock.types.inference_profile_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetInferenceProfileResponse.status required")
    if "type" in data:
        import aws_sdk_bedrock.types.inference_profile_type

        out["type"] = aws_sdk_bedrock.types.inference_profile_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetInferenceProfileResponse.type required")
    return out
