"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.timestamp


class UpdateWorkspaceResponse(TypedDict):
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time of the current update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceResponse:
    out: UpdateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("UpdateWorkspaceResponse.update_date_time required")
    return out
