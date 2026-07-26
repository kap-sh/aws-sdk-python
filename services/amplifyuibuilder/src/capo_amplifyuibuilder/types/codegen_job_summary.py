"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.uuid


class CodegenJobSummary(TypedDict, closed=True):
    app_id: "capo_amplifyuibuilder.types.app_id.AppId"
    """<p>The unique ID of the Amplify app associated with the code generation job.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment associated with the code generation job.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the code generation job summary.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job summary was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job summary was modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    if "created_at" in value:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["createdAt"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["modifiedAt"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["modified_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodegenJobSummary:
    out: CodegenJobSummary = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("CodegenJobSummary.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("CodegenJobSummary.environment_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CodegenJobSummary.id required")
    if "createdAt" in data:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["created_at"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["modified_at"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    return out
