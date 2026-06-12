"""Generated from Smithy shape ``com.amazonaws.amplify#GetBackendEnvironmentResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.backend_environment


class GetBackendEnvironmentResult(TypedDict):
    backend_environment: "aws_sdk_amplify.types.backend_environment.BackendEnvironment"
    """<p>Describes the backend environment for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendEnvironmentResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.backend_environment

    out["backendEnvironment"] = (
        aws_sdk_amplify.types.backend_environment.serialize_json(
            value["backend_environment"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBackendEnvironmentResult:
    out: GetBackendEnvironmentResult = {}  # type: ignore[typeddict-item]
    if "backendEnvironment" in data:
        import aws_sdk_amplify.types.backend_environment

        out["backend_environment"] = (
            aws_sdk_amplify.types.backend_environment.deserialize_json(
                data["backendEnvironment"]
            )
        )
    else:
        raise DeserializationError(
            "GetBackendEnvironmentResult.backend_environment required"
        )
    return out
