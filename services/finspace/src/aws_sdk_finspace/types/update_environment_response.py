"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.environment


class UpdateEnvironmentResponse(TypedDict):
    environment: NotRequired["aws_sdk_finspace.types.environment.Environment"]
    """<p>Returns the FinSpace environment object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_finspace.types.environment

        out["environment"] = aws_sdk_finspace.types.environment.serialize_json(
            value["environment"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentResponse:
    out: UpdateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_finspace.types.environment

        out["environment"] = aws_sdk_finspace.types.environment.deserialize_json(
            data["environment"]
        )
    return out
