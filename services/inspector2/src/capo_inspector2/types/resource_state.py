"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.state

ResourceState = TypedDict(
    "ResourceState",
    {
        "ec2": "capo_inspector2.types.state.State",
        "ecr": "capo_inspector2.types.state.State",
        "lambda": NotRequired["capo_inspector2.types.state.State"],
        "lambda_code": NotRequired["capo_inspector2.types.state.State"],
        "code_repository": NotRequired["capo_inspector2.types.state.State"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceState) -> dict:
    out: dict = {}
    import capo_inspector2.types.state

    out["ec2"] = capo_inspector2.types.state.serialize_json(value["ec2"])
    import capo_inspector2.types.state

    out["ecr"] = capo_inspector2.types.state.serialize_json(value["ecr"])
    if "lambda" in value:
        import capo_inspector2.types.state

        out["lambda"] = capo_inspector2.types.state.serialize_json(value["lambda"])
    if "lambda_code" in value:
        import capo_inspector2.types.state

        out["lambdaCode"] = capo_inspector2.types.state.serialize_json(
            value["lambda_code"]
        )
    if "code_repository" in value:
        import capo_inspector2.types.state

        out["codeRepository"] = capo_inspector2.types.state.serialize_json(
            value["code_repository"]
        )
    return out


def deserialize_json(data: dict) -> ResourceState:
    out: ResourceState = {}  # type: ignore[typeddict-item]
    if "ec2" in data:
        import capo_inspector2.types.state

        out["ec2"] = capo_inspector2.types.state.deserialize_json(data["ec2"])
    else:
        raise DeserializationError("ResourceState.ec2 required")
    if "ecr" in data:
        import capo_inspector2.types.state

        out["ecr"] = capo_inspector2.types.state.deserialize_json(data["ecr"])
    else:
        raise DeserializationError("ResourceState.ecr required")
    if "lambda" in data:
        import capo_inspector2.types.state

        out["lambda"] = capo_inspector2.types.state.deserialize_json(data["lambda"])
    if "lambdaCode" in data:
        import capo_inspector2.types.state

        out["lambda_code"] = capo_inspector2.types.state.deserialize_json(
            data["lambdaCode"]
        )
    if "codeRepository" in data:
        import capo_inspector2.types.state

        out["code_repository"] = capo_inspector2.types.state.deserialize_json(
            data["codeRepository"]
        )
    return out
