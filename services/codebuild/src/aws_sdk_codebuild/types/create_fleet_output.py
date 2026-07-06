"""Generated from Smithy shape ``com.amazonaws.codebuild#CreateFleetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet


class CreateFleetOutput(TypedDict, closed=True):
    fleet: NotRequired["aws_sdk_codebuild.types.fleet.Fleet"]
    """<p>Information about the compute fleet</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetOutput) -> dict:
    out: dict = {}
    if "fleet" in value:
        import aws_sdk_codebuild.types.fleet

        out["fleet"] = aws_sdk_codebuild.types.fleet.serialize_aws_json_1_1(
            value["fleet"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetOutput:
    out: CreateFleetOutput = {}  # type: ignore[typeddict-item]
    if "fleet" in data:
        import aws_sdk_codebuild.types.fleet

        out["fleet"] = aws_sdk_codebuild.types.fleet.deserialize_aws_json_1_1(
            data["fleet"]
        )
    return out
