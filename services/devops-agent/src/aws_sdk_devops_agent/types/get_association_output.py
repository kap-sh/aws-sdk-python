"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssociationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.association


class GetAssociationOutput(TypedDict):
    association: "aws_sdk_devops_agent.types.association.Association"


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociationOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.association

    out["association"] = aws_sdk_devops_agent.types.association.serialize_json(
        value["association"]
    )
    return out


def deserialize_json(data: dict) -> GetAssociationOutput:
    out: GetAssociationOutput = {}  # type: ignore[typeddict-item]
    if "association" in data:
        import aws_sdk_devops_agent.types.association

        out["association"] = aws_sdk_devops_agent.types.association.deserialize_json(
            data["association"]
        )
    else:
        raise DeserializationError("GetAssociationOutput.association required")
    return out
