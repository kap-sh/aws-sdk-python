"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.state

ResourceState = TypedDict(
    "ResourceState",
    {
        "ec2": "aws_sdk_inspector2.types.state.State",
        "ecr": "aws_sdk_inspector2.types.state.State",
        "lambda": NotRequired["aws_sdk_inspector2.types.state.State"],
        "lambda_code": NotRequired["aws_sdk_inspector2.types.state.State"],
        "code_repository": NotRequired["aws_sdk_inspector2.types.state.State"],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceState) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.state

    out["ec2"] = aws_sdk_inspector2.types.state.serialize_json(value["ec2"])
    import aws_sdk_inspector2.types.state

    out["ecr"] = aws_sdk_inspector2.types.state.serialize_json(value["ecr"])
    if "lambda" in value:
        import aws_sdk_inspector2.types.state

        out["lambda"] = aws_sdk_inspector2.types.state.serialize_json(value["lambda"])
    if "lambda_code" in value:
        import aws_sdk_inspector2.types.state

        out["lambdaCode"] = aws_sdk_inspector2.types.state.serialize_json(
            value["lambda_code"]
        )
    if "code_repository" in value:
        import aws_sdk_inspector2.types.state

        out["codeRepository"] = aws_sdk_inspector2.types.state.serialize_json(
            value["code_repository"]
        )
    return out


def deserialize_json(data: dict) -> ResourceState:
    out: ResourceState = {}  # type: ignore[typeddict-item]
    if "ec2" in data:
        import aws_sdk_inspector2.types.state

        out["ec2"] = aws_sdk_inspector2.types.state.deserialize_json(data["ec2"])
    else:
        raise DeserializationError("ResourceState.ec2 required")
    if "ecr" in data:
        import aws_sdk_inspector2.types.state

        out["ecr"] = aws_sdk_inspector2.types.state.deserialize_json(data["ecr"])
    else:
        raise DeserializationError("ResourceState.ecr required")
    if "lambda" in data:
        import aws_sdk_inspector2.types.state

        out["lambda"] = aws_sdk_inspector2.types.state.deserialize_json(data["lambda"])
    if "lambdaCode" in data:
        import aws_sdk_inspector2.types.state

        out["lambda_code"] = aws_sdk_inspector2.types.state.deserialize_json(
            data["lambdaCode"]
        )
    if "codeRepository" in data:
        import aws_sdk_inspector2.types.state

        out["code_repository"] = aws_sdk_inspector2.types.state.deserialize_json(
            data["codeRepository"]
        )
    return out
