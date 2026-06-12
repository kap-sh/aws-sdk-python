"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppSessionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_value_list
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class UpdateQAppSessionInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App session to provide input for.</p>"""
    values: NotRequired["aws_sdk_qapps.types.card_value_list.CardValueList"]
    """<p>The input values to provide for the current state of the Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppSessionInput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "values" in value:
        import aws_sdk_qapps.types.card_value_list

        out["values"] = aws_sdk_qapps.types.card_value_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppSessionInput:
    out: UpdateQAppSessionInput = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("UpdateQAppSessionInput.session_id required")
    if "values" in data:
        import aws_sdk_qapps.types.card_value_list

        out["values"] = aws_sdk_qapps.types.card_value_list.deserialize_json(
            data["values"]
        )
    return out
