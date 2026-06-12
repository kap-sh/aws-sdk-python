"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteBackendEnvironmentResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.backend_environment


class DeleteBackendEnvironmentResult(TypedDict):
    backend_environment: "aws_sdk_amplify.types.backend_environment.BackendEnvironment"
    """<p>Describes the backend environment for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackendEnvironmentResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.backend_environment

    out["backendEnvironment"] = (
        aws_sdk_amplify.types.backend_environment.serialize_json(
            value["backend_environment"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteBackendEnvironmentResult:
    out: DeleteBackendEnvironmentResult = {}  # type: ignore[typeddict-item]
    if "backendEnvironment" in data:
        import aws_sdk_amplify.types.backend_environment

        out["backend_environment"] = (
            aws_sdk_amplify.types.backend_environment.deserialize_json(
                data["backendEnvironment"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteBackendEnvironmentResult.backend_environment required"
        )
    return out
