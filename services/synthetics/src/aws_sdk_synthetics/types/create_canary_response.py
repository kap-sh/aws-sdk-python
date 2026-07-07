"""Generated from Smithy shape ``com.amazonaws.synthetics#CreateCanaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary


class CreateCanaryResponse(TypedDict, closed=True):
    canary: NotRequired["aws_sdk_synthetics.types.canary.Canary"]
    """<p>The full details about the canary you have created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCanaryResponse) -> dict:
    out: dict = {}
    if "canary" in value:
        import aws_sdk_synthetics.types.canary

        out["Canary"] = aws_sdk_synthetics.types.canary.serialize_json(value["canary"])
    return out


def deserialize_json(data: dict) -> CreateCanaryResponse:
    out: CreateCanaryResponse = {}  # type: ignore[typeddict-item]
    if "Canary" in data:
        import aws_sdk_synthetics.types.canary

        out["canary"] = aws_sdk_synthetics.types.canary.deserialize_json(data["Canary"])
    return out
