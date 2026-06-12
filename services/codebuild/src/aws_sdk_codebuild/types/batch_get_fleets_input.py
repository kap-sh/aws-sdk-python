"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetFleetsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_names


class BatchGetFleetsInput(TypedDict):
    names: "aws_sdk_codebuild.types.fleet_names.FleetNames"
    """<p>The names or ARNs of the compute fleets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetFleetsInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.fleet_names

    out["names"] = aws_sdk_codebuild.types.fleet_names.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetFleetsInput:
    out: BatchGetFleetsInput = {}  # type: ignore[typeddict-item]
    if "names" in data:
        import aws_sdk_codebuild.types.fleet_names

        out["names"] = aws_sdk_codebuild.types.fleet_names.deserialize_aws_json_1_1(
            data["names"]
        )
    else:
        raise DeserializationError("BatchGetFleetsInput.names required")
    return out
