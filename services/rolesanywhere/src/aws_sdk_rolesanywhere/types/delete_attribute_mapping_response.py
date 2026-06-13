"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#DeleteAttributeMappingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.profile_detail


class DeleteAttributeMappingResponse(TypedDict):
    profile: "aws_sdk_rolesanywhere.types.profile_detail.ProfileDetail"
    """<p>The state of the profile after a read or write operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttributeMappingResponse) -> dict:
    out: dict = {}
    import aws_sdk_rolesanywhere.types.profile_detail

    out["profile"] = aws_sdk_rolesanywhere.types.profile_detail.serialize_json(
        value["profile"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAttributeMappingResponse:
    out: DeleteAttributeMappingResponse = {}  # type: ignore[typeddict-item]
    if "profile" in data:
        import aws_sdk_rolesanywhere.types.profile_detail

        out["profile"] = aws_sdk_rolesanywhere.types.profile_detail.deserialize_json(
            data["profile"]
        )
    else:
        raise DeserializationError("DeleteAttributeMappingResponse.profile required")
    return out
