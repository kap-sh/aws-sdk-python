"""Generated from Smithy shape ``com.amazonaws.proton#CancelEnvironmentDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment


class CancelEnvironmentDeploymentOutput(TypedDict, closed=True):
    environment: "aws_sdk_proton.types.environment.Environment"
    """<p>The environment summary data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelEnvironmentDeploymentOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.environment

    out["environment"] = aws_sdk_proton.types.environment.serialize_aws_json_1_0(
        value["environment"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelEnvironmentDeploymentOutput:
    out: CancelEnvironmentDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_proton.types.environment

        out["environment"] = aws_sdk_proton.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    else:
        raise DeserializationError(
            "CancelEnvironmentDeploymentOutput.environment required"
        )
    return out
