"""Generated from Smithy shape ``com.amazonaws.mwaa#GetEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment


class GetEnvironmentOutput(TypedDict, closed=True):
    environment: NotRequired["aws_sdk_mwaa.types.environment.Environment"]
    """<p>An object containing all available details about the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentOutput) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_mwaa.types.environment

        out["Environment"] = aws_sdk_mwaa.types.environment.serialize_json(
            value["environment"]
        )
    return out


def deserialize_json(data: dict) -> GetEnvironmentOutput:
    out: GetEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "Environment" in data:
        import aws_sdk_mwaa.types.environment

        out["environment"] = aws_sdk_mwaa.types.environment.deserialize_json(
            data["Environment"]
        )
    return out
