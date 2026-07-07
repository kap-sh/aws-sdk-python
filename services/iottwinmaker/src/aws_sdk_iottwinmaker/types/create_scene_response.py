"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSceneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class CreateSceneResponse(TypedDict, closed=True):
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the scene.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSceneResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateSceneResponse:
    out: CreateSceneResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSceneResponse.arn required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("CreateSceneResponse.creation_date_time required")
    return out
