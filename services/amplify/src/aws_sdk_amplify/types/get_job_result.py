"""Generated from Smithy shape ``com.amazonaws.amplify#GetJobResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.job


class GetJobResult(TypedDict):
    job: "aws_sdk_amplify.types.job.Job"


# --- restJson1 ser/de ---
def serialize_json(value: GetJobResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.job

    out["job"] = aws_sdk_amplify.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> GetJobResult:
    out: GetJobResult = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_amplify.types.job

        out["job"] = aws_sdk_amplify.types.job.deserialize_json(data["job"])
    else:
        raise DeserializationError("GetJobResult.job required")
    return out
