"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AssociateSourceToS3TableIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.data_source


class AssociateSourceToS3TableIntegrationRequest(TypedDict, closed=True):
    integration_arn: "aws_sdk_cloudwatch_logs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the S3 Table Integration to associate the data source with.</p>"""
    data_source: "aws_sdk_cloudwatch_logs.types.data_source.DataSource"
    """<p>The data source to associate with the S3 Table Integration. Contains the name and type of the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateSourceToS3TableIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import aws_sdk_cloudwatch_logs.types.data_source

    out["dataSource"] = (
        aws_sdk_cloudwatch_logs.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateSourceToS3TableIntegrationRequest:
    out: AssociateSourceToS3TableIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "AssociateSourceToS3TableIntegrationRequest.integration_arn required"
        )
    if "dataSource" in data:
        import aws_sdk_cloudwatch_logs.types.data_source

        out["data_source"] = (
            aws_sdk_cloudwatch_logs.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateSourceToS3TableIntegrationRequest.data_source required"
        )
    return out
