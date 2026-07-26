"""Generated from Smithy shape ``com.amazonaws.amplify#ListBackendEnvironmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.backend_environments
    import capo_amplify.types.next_token


class ListBackendEnvironmentsResult(TypedDict, closed=True):
    backend_environments: "capo_amplify.types.backend_environments.BackendEnvironments"
    """<p>The list of backend environments for an Amplify app. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackendEnvironmentsResult) -> dict:
    out: dict = {}
    import capo_amplify.types.backend_environments

    out["backendEnvironments"] = capo_amplify.types.backend_environments.serialize_json(
        value["backend_environments"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBackendEnvironmentsResult:
    out: ListBackendEnvironmentsResult = {}  # type: ignore[typeddict-item]
    if "backendEnvironments" in data:
        import capo_amplify.types.backend_environments

        out["backend_environments"] = (
            capo_amplify.types.backend_environments.deserialize_json(
                data["backendEnvironments"]
            )
        )
    else:
        raise DeserializationError(
            "ListBackendEnvironmentsResult.backend_environments required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
