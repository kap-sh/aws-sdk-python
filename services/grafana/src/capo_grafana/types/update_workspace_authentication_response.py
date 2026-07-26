"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceAuthenticationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.authentication_description


class UpdateWorkspaceAuthenticationResponse(TypedDict, closed=True):
    authentication: (
        "capo_grafana.types.authentication_description.AuthenticationDescription"
    )
    """<p>A structure that describes the user authentication for this workspace after the update is made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceAuthenticationResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.authentication_description

    out["authentication"] = (
        capo_grafana.types.authentication_description.serialize_json(
            value["authentication"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceAuthenticationResponse:
    out: UpdateWorkspaceAuthenticationResponse = {}  # type: ignore[typeddict-item]
    if "authentication" in data:
        import capo_grafana.types.authentication_description

        out["authentication"] = (
            capo_grafana.types.authentication_description.deserialize_json(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkspaceAuthenticationResponse.authentication required"
        )
    return out
