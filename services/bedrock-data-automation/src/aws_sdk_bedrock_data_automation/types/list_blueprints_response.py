"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListBlueprintsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprints
    import aws_sdk_bedrock_data_automation.types.next_token


class ListBlueprintsResponse(TypedDict):
    blueprints: "aws_sdk_bedrock_data_automation.types.blueprints.Blueprints"
    next_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListBlueprintsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.blueprints

    out["blueprints"] = aws_sdk_bedrock_data_automation.types.blueprints.serialize_json(
        value["blueprints"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBlueprintsResponse:
    out: ListBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if "blueprints" in data:
        import aws_sdk_bedrock_data_automation.types.blueprints

        out["blueprints"] = (
            aws_sdk_bedrock_data_automation.types.blueprints.deserialize_json(
                data["blueprints"]
            )
        )
    else:
        raise DeserializationError("ListBlueprintsResponse.blueprints required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
