"""Generated from Smithy shape ``com.amazonaws.inspector2#AutoEnable``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_inspector2.errors import DeserializationError

AutoEnable = TypedDict("AutoEnable", {
    "ec2": "bool",
    "ecr": "bool",
    "lambda": NotRequired["bool"],
    "lambda_code": NotRequired["bool"],
    "code_repository": NotRequired["bool"],
})

# --- restJson1 ser/de ---
def serialize_json(value: AutoEnable) -> dict:
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


def deserialize_json(data: dict) -> AutoEnable:
    out: AutoEnable = {}  # type: ignore[typeddict-item]
    if "ec2" in data:
        out["ec2"] = data["ec2"]
    else:
        raise DeserializationError("AutoEnable.ec2 required")
    if "ecr" in data:
        out["ecr"] = data["ecr"]
    else:
        raise DeserializationError("AutoEnable.ecr required")
    if "lambda" in data:
        out["lambda"] = data["lambda"]
    if "lambdaCode" in data:
        out["lambda_code"] = data["lambdaCode"]
    if "codeRepository" in data:
        out["code_repository"] = data["codeRepository"]
    return out