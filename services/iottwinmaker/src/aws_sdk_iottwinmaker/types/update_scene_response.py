"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateSceneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.timestamp


class UpdateSceneResponse(TypedDict, closed=True):
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSceneResponse) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSceneResponse:
    out: UpdateSceneResponse = {}  # type: ignore[typeddict-item]
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("UpdateSceneResponse.update_date_time required")
    return out
