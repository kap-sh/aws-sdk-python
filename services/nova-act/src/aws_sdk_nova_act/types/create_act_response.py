"""Generated from Smithy shape ``com.amazonaws.novaact#CreateActResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.act_status
    import aws_sdk_nova_act.types.uuid_string


class CreateActResponse(TypedDict):
    act_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for the created act.</p>"""
    status: "aws_sdk_nova_act.types.act_status.ActStatus"
    """<p>The initial status of the act after creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActResponse) -> dict:
    out: dict = {}
    out["actId"] = value["act_id"]
    import aws_sdk_nova_act.types.act_status

    out["status"] = aws_sdk_nova_act.types.act_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateActResponse:
    out: CreateActResponse = {}  # type: ignore[typeddict-item]
    if "actId" in data:
        out["act_id"] = data["actId"]
    else:
        raise DeserializationError("CreateActResponse.act_id required")
    if "status" in data:
        import aws_sdk_nova_act.types.act_status

        out["status"] = aws_sdk_nova_act.types.act_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateActResponse.status required")
    return out
