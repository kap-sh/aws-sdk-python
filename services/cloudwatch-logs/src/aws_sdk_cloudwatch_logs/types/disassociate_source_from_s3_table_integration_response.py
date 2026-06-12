"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DisassociateSourceFromS3TableIntegrationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.s3_table_integration_source_identifier


class DisassociateSourceFromS3TableIntegrationResponse(TypedDict):
    identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier"
    ]
    """<p>The unique identifier of the association that was removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateSourceFromS3TableIntegrationResponse,
) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateSourceFromS3TableIntegrationResponse:
    out: DisassociateSourceFromS3TableIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    return out
