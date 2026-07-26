"""Generated from Smithy shape ``com.amazonaws.ssm#OutputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.output_source_id
    import capo_ssm.types.output_source_type


class OutputSource(TypedDict, closed=True):
    output_source_id: NotRequired["capo_ssm.types.output_source_id.OutputSourceId"]
    """<p>The ID of the output source, for example the URL of an S3 bucket.</p>"""
    output_source_type: NotRequired[
        "capo_ssm.types.output_source_type.OutputSourceType"
    ]
    """<p>The type of source where the association execution details are stored, for example, Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputSource) -> dict:
    out: dict = {}
    if "output_source_id" in value:
        out["OutputSourceId"] = value["output_source_id"]
    if "output_source_type" in value:
        out["OutputSourceType"] = value["output_source_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputSource:
    out: OutputSource = {}  # type: ignore[typeddict-item]
    if "OutputSourceId" in data:
        out["output_source_id"] = data["OutputSourceId"]
    if "OutputSourceType" in data:
        out["output_source_type"] = data["OutputSourceType"]
    return out
