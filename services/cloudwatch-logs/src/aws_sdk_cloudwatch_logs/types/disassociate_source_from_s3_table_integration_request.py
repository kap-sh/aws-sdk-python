"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DisassociateSourceFromS3TableIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.s3_table_integration_source_identifier


class DisassociateSourceFromS3TableIntegrationRequest(TypedDict):
    identifier: "aws_sdk_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier"
    """<p>The unique identifier of the association to remove between the data source and S3 Table Integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateSourceFromS3TableIntegrationRequest,
) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateSourceFromS3TableIntegrationRequest:
    out: DisassociateSourceFromS3TableIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError(
            "DisassociateSourceFromS3TableIntegrationRequest.identifier required"
        )
    return out
