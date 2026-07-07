"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateComponentTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.state
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class CreateComponentTypeResponse(TypedDict, closed=True):
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the component type.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was created.</p>"""
    state: "aws_sdk_iottwinmaker.types.state.State"
    """<p>The current state of the component type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentTypeResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> CreateComponentTypeResponse:
    out: CreateComponentTypeResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateComponentTypeResponse.arn required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CreateComponentTypeResponse.creation_date_time required"
        )
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("CreateComponentTypeResponse.state required")
    return out
