"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServicePipelineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_pipeline


class UpdateServicePipelineOutput(TypedDict):
    pipeline: "aws_sdk_proton.types.service_pipeline.ServicePipeline"
    """<p>The pipeline details that are returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServicePipelineOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service_pipeline

    out["pipeline"] = aws_sdk_proton.types.service_pipeline.serialize_aws_json_1_0(
        value["pipeline"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServicePipelineOutput:
    out: UpdateServicePipelineOutput = {}  # type: ignore[typeddict-item]
    if "pipeline" in data:
        import aws_sdk_proton.types.service_pipeline

        out["pipeline"] = (
            aws_sdk_proton.types.service_pipeline.deserialize_aws_json_1_0(
                data["pipeline"]
            )
        )
    else:
        raise DeserializationError("UpdateServicePipelineOutput.pipeline required")
    return out
