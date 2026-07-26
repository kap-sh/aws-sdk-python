"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DisassociateSourceFromS3TableIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.s3_table_integration_source_identifier


class DisassociateSourceFromS3TableIntegrationResponse(TypedDict, closed=True):
    identifier: NotRequired[
        "capo_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier"
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
