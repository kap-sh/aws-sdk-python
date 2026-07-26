"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAPIResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.backend_api_auth_type
    import capo_amplifybackend.types.backend_api_conflict_resolution
    import capo_amplifybackend.types.list_of_backend_api_auth_type


class BackendAPIResourceConfig(TypedDict, closed=True):
    additional_auth_types: NotRequired[
        "capo_amplifybackend.types.list_of_backend_api_auth_type.ListOfBackendAPIAuthType"
    ]
    """<p>Additional authentication methods used to interact with your data models.</p>"""
    api_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The API name used to interact with the data model, configured as a part of your Amplify project.</p>"""
    conflict_resolution: NotRequired[
        "capo_amplifybackend.types.backend_api_conflict_resolution.BackendAPIConflictResolution"
    ]
    """<p>The conflict resolution strategy for your data stored in the data models.</p>"""
    default_auth_type: NotRequired[
        "capo_amplifybackend.types.backend_api_auth_type.BackendAPIAuthType"
    ]
    """<p>The default authentication type for interacting with the configured data models in your Amplify project.</p>"""
    service: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The service used to provision and interact with the data model.</p>"""
    transform_schema: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The definition of the data model in the annotated transform of the GraphQL schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAPIResourceConfig) -> dict:
    out: dict = {}
    if "additional_auth_types" in value:
        import capo_amplifybackend.types.list_of_backend_api_auth_type

        out["additionalAuthTypes"] = (
            capo_amplifybackend.types.list_of_backend_api_auth_type.serialize_json(
                value["additional_auth_types"]
            )
        )
    if "api_name" in value:
        out["apiName"] = value["api_name"]
    if "conflict_resolution" in value:
        import capo_amplifybackend.types.backend_api_conflict_resolution

        out["conflictResolution"] = (
            capo_amplifybackend.types.backend_api_conflict_resolution.serialize_json(
                value["conflict_resolution"]
            )
        )
    if "default_auth_type" in value:
        import capo_amplifybackend.types.backend_api_auth_type

        out["defaultAuthType"] = (
            capo_amplifybackend.types.backend_api_auth_type.serialize_json(
                value["default_auth_type"]
            )
        )
    if "service" in value:
        out["service"] = value["service"]
    if "transform_schema" in value:
        out["transformSchema"] = value["transform_schema"]
    return out


def deserialize_json(data: dict) -> BackendAPIResourceConfig:
    out: BackendAPIResourceConfig = {}  # type: ignore[typeddict-item]
    if "additionalAuthTypes" in data:
        import capo_amplifybackend.types.list_of_backend_api_auth_type

        out["additional_auth_types"] = (
            capo_amplifybackend.types.list_of_backend_api_auth_type.deserialize_json(
                data["additionalAuthTypes"]
            )
        )
    if "apiName" in data:
        out["api_name"] = data["apiName"]
    if "conflictResolution" in data:
        import capo_amplifybackend.types.backend_api_conflict_resolution

        out["conflict_resolution"] = (
            capo_amplifybackend.types.backend_api_conflict_resolution.deserialize_json(
                data["conflictResolution"]
            )
        )
    if "defaultAuthType" in data:
        import capo_amplifybackend.types.backend_api_auth_type

        out["default_auth_type"] = (
            capo_amplifybackend.types.backend_api_auth_type.deserialize_json(
                data["defaultAuthType"]
            )
        )
    if "service" in data:
        out["service"] = data["service"]
    if "transformSchema" in data:
        out["transform_schema"] = data["transformSchema"]
    return out
