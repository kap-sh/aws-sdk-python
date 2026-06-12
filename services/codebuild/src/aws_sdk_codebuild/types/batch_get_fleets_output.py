"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetFleetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_names
    import aws_sdk_codebuild.types.fleets


class BatchGetFleetsOutput(TypedDict):
    fleets: NotRequired["aws_sdk_codebuild.types.fleets.Fleets"]
    """<p>Information about the requested compute fleets.</p>"""
    fleets_not_found: NotRequired["aws_sdk_codebuild.types.fleet_names.FleetNames"]
    """<p>The names of compute fleets for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetFleetsOutput) -> dict:
    out: dict = {}
    if "fleets" in value:
        import aws_sdk_codebuild.types.fleets

        out["fleets"] = aws_sdk_codebuild.types.fleets.serialize_aws_json_1_1(
            value["fleets"]
        )
    if "fleets_not_found" in value:
        import aws_sdk_codebuild.types.fleet_names

        out["fleetsNotFound"] = (
            aws_sdk_codebuild.types.fleet_names.serialize_aws_json_1_1(
                value["fleets_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetFleetsOutput:
    out: BatchGetFleetsOutput = {}  # type: ignore[typeddict-item]
    if "fleets" in data:
        import aws_sdk_codebuild.types.fleets

        out["fleets"] = aws_sdk_codebuild.types.fleets.deserialize_aws_json_1_1(
            data["fleets"]
        )
    if "fleetsNotFound" in data:
        import aws_sdk_codebuild.types.fleet_names

        out["fleets_not_found"] = (
            aws_sdk_codebuild.types.fleet_names.deserialize_aws_json_1_1(
                data["fleetsNotFound"]
            )
        )
    return out
