"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment


class GetEnvironmentOutput(TypedDict):
    environment: "aws_sdk_proton.types.environment.Environment"
    """<p>The detailed data of the requested environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.environment

    out["environment"] = aws_sdk_proton.types.environment.serialize_aws_json_1_0(
        value["environment"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentOutput:
    out: GetEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_proton.types.environment

        out["environment"] = aws_sdk_proton.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    else:
        raise DeserializationError("GetEnvironmentOutput.environment required")
    return out
