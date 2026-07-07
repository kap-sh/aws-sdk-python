"""Generated from Smithy shape ``com.amazonaws.finspace#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.environment


class GetEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired["aws_sdk_finspace.types.environment.Environment"]
    """<p>The name of the FinSpace environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_finspace.types.environment

        out["environment"] = aws_sdk_finspace.types.environment.serialize_json(
            value["environment"]
        )
    return out


def deserialize_json(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_finspace.types.environment

        out["environment"] = aws_sdk_finspace.types.environment.deserialize_json(
            data["environment"]
        )
    return out
