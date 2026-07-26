"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetFleetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_names


class BatchGetFleetsInput(TypedDict, closed=True):
    names: "capo_codebuild.types.fleet_names.FleetNames"
    """<p>The names or ARNs of the compute fleets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetFleetsInput) -> dict:
    out: dict = {}
    import capo_codebuild.types.fleet_names

    out["names"] = capo_codebuild.types.fleet_names.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetFleetsInput:
    out: BatchGetFleetsInput = {}  # type: ignore[typeddict-item]
    if "names" in data:
        import capo_codebuild.types.fleet_names

        out["names"] = capo_codebuild.types.fleet_names.deserialize_aws_json_1_1(
            data["names"]
        )
    else:
        raise DeserializationError("BatchGetFleetsInput.names required")
    return out
