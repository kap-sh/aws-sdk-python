"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment


class DeleteEnvironmentOutput(TypedDict, closed=True):
    environment: NotRequired["aws_sdk_proton.types.environment.Environment"]
    """<p>The detailed data of the environment being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentOutput) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_proton.types.environment

        out["environment"] = aws_sdk_proton.types.environment.serialize_aws_json_1_0(
            value["environment"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentOutput:
    out: DeleteEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_proton.types.environment

        out["environment"] = aws_sdk_proton.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    return out
