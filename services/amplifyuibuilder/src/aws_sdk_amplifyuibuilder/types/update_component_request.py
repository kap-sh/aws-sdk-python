"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateComponentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.update_component_data
    import aws_sdk_amplifyuibuilder.types.uuid


class UpdateComponentRequest(TypedDict):
    app_id: "str"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the component.</p>"""
    client_token: NotRequired["str"]
    """<p>The unique client token.</p>"""
    updated_component: (
        "aws_sdk_amplifyuibuilder.types.update_component_data.UpdateComponentData"
    )
    """<p>The configuration of the updated component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComponentRequest) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.update_component_data

    out["updatedComponent"] = (
        aws_sdk_amplifyuibuilder.types.update_component_data.serialize_json(
            value["updated_component"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateComponentRequest:
    out: UpdateComponentRequest = {}  # type: ignore[typeddict-item]
    if "updatedComponent" in data:
        import aws_sdk_amplifyuibuilder.types.update_component_data

        out["updated_component"] = (
            aws_sdk_amplifyuibuilder.types.update_component_data.deserialize_json(
                data["updatedComponent"]
            )
        )
    else:
        raise DeserializationError("UpdateComponentRequest.updated_component required")
    return out
