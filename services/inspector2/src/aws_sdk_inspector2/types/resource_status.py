"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.status

ResourceStatus = TypedDict(
    "ResourceStatus",
    {
        "ec2": "aws_sdk_inspector2.types.status.Status",
        "ecr": "aws_sdk_inspector2.types.status.Status",
        "lambda": NotRequired["aws_sdk_inspector2.types.status.Status"],
        "lambda_code": NotRequired["aws_sdk_inspector2.types.status.Status"],
        "code_repository": NotRequired["aws_sdk_inspector2.types.status.Status"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> dict:
    out: dict = {}
    out["ec2"] = value["ec2"]
    out["ecr"] = value["ecr"]
    if "lambda" in value:
        out["lambda"] = value["lambda"]
    if "lambda_code" in value:
        out["lambdaCode"] = value["lambda_code"]
    if "code_repository" in value:
        out["codeRepository"] = value["code_repository"]
    return out


def deserialize_json(data: dict) -> ResourceStatus:
    out: ResourceStatus = {}  # type: ignore[typeddict-item]
    if "ec2" in data:
        out["ec2"] = data["ec2"]
    else:
        raise DeserializationError("ResourceStatus.ec2 required")
    if "ecr" in data:
        out["ecr"] = data["ecr"]
    else:
        raise DeserializationError("ResourceStatus.ecr required")
    if "lambda" in data:
        out["lambda"] = data["lambda"]
    if "lambdaCode" in data:
        out["lambda_code"] = data["lambdaCode"]
    if "codeRepository" in data:
        out["code_repository"] = data["codeRepository"]
    return out
