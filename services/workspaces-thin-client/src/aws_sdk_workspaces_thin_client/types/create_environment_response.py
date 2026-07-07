"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#CreateEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.environment_summary


class CreateEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired[
        "aws_sdk_workspaces_thin_client.types.environment_summary.EnvironmentSummary"
    ]
    """<p>Describes an environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_workspaces_thin_client.types.environment_summary

        out["environment"] = (
            aws_sdk_workspaces_thin_client.types.environment_summary.serialize_json(
                value["environment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentResponse:
    out: CreateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_workspaces_thin_client.types.environment_summary

        out["environment"] = (
            aws_sdk_workspaces_thin_client.types.environment_summary.deserialize_json(
                data["environment"]
            )
        )
    return out
