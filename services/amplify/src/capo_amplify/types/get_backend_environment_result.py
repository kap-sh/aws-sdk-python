"""Generated from Smithy shape ``com.amazonaws.amplify#GetBackendEnvironmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.backend_environment


class GetBackendEnvironmentResult(TypedDict, closed=True):
    backend_environment: "capo_amplify.types.backend_environment.BackendEnvironment"
    """<p>Describes the backend environment for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendEnvironmentResult) -> dict:
    out: dict = {}
    import capo_amplify.types.backend_environment

    out["backendEnvironment"] = capo_amplify.types.backend_environment.serialize_json(
        value["backend_environment"]
    )
    return out


def deserialize_json(data: dict) -> GetBackendEnvironmentResult:
    out: GetBackendEnvironmentResult = {}  # type: ignore[typeddict-item]
    if "backendEnvironment" in data:
        import capo_amplify.types.backend_environment

        out["backend_environment"] = (
            capo_amplify.types.backend_environment.deserialize_json(
                data["backendEnvironment"]
            )
        )
    else:
        raise DeserializationError(
            "GetBackendEnvironmentResult.backend_environment required"
        )
    return out
