"""Generated from Smithy shape ``com.amazonaws.gamelift#RegisterComputeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.compute


class RegisterComputeOutput(TypedDict, closed=True):
    compute: NotRequired["aws_sdk_gamelift.types.compute.Compute"]
    """<p>The details of the compute resource you registered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterComputeOutput) -> dict:
    out: dict = {}
    if "compute" in value:
        import aws_sdk_gamelift.types.compute

        out["Compute"] = aws_sdk_gamelift.types.compute.serialize_aws_json_1_1(
            value["compute"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterComputeOutput:
    out: RegisterComputeOutput = {}  # type: ignore[typeddict-item]
    if "Compute" in data:
        import aws_sdk_gamelift.types.compute

        out["compute"] = aws_sdk_gamelift.types.compute.deserialize_aws_json_1_1(
            data["Compute"]
        )
    return out
