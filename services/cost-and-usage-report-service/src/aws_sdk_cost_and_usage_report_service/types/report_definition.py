"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.additional_artifact_list
    import aws_sdk_cost_and_usage_report_service.types.aws_region
    import aws_sdk_cost_and_usage_report_service.types.billing_view_arn
    import aws_sdk_cost_and_usage_report_service.types.compression_format
    import aws_sdk_cost_and_usage_report_service.types.refresh_closed_reports
    import aws_sdk_cost_and_usage_report_service.types.report_format
    import aws_sdk_cost_and_usage_report_service.types.report_name
    import aws_sdk_cost_and_usage_report_service.types.report_status
    import aws_sdk_cost_and_usage_report_service.types.report_versioning
    import aws_sdk_cost_and_usage_report_service.types.s3_bucket
    import aws_sdk_cost_and_usage_report_service.types.s3_prefix
    import aws_sdk_cost_and_usage_report_service.types.schema_element_list
    import aws_sdk_cost_and_usage_report_service.types.time_unit


class ReportDefinition(TypedDict, closed=True):
    report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName"
    time_unit: "aws_sdk_cost_and_usage_report_service.types.time_unit.TimeUnit"
    format: "aws_sdk_cost_and_usage_report_service.types.report_format.ReportFormat"
    compression: "aws_sdk_cost_and_usage_report_service.types.compression_format.CompressionFormat"
    additional_schema_elements: "aws_sdk_cost_and_usage_report_service.types.schema_element_list.SchemaElementList"
    """<p>A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs. </p>"""
    s3_bucket: "aws_sdk_cost_and_usage_report_service.types.s3_bucket.S3Bucket"
    s3_prefix: "aws_sdk_cost_and_usage_report_service.types.s3_prefix.S3Prefix"
    s3_region: "aws_sdk_cost_and_usage_report_service.types.aws_region.AWSRegion"
    additional_artifacts: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.additional_artifact_list.AdditionalArtifactList"
    ]
    """<p>A list of manifests that you want Amazon Web Services to create for this report.</p>"""
    refresh_closed_reports: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.refresh_closed_reports.RefreshClosedReports"
    ]
    """<p>Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.</p>"""
    report_versioning: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.report_versioning.ReportVersioning"
    ]
    """<p>Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.</p>"""
    billing_view_arn: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.billing_view_arn.BillingViewArn"
    ]
    """<p> The Amazon resource name of the billing view. The <code>BillingViewArn</code> is needed to create Amazon Web Services Cost and Usage Report for each billing group maintained in the Amazon Web Services Billing Conductor service. The <code>BillingViewArn</code> for a billing group can be constructed as: <code>arn:aws:billing::payer-account-id:billingview/billing-group-primary-account-id</code> </p>"""
    report_status: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.report_status.ReportStatus"
    ]
    """<p>The status of the report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportDefinition) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import aws_sdk_cost_and_usage_report_service.types.time_unit

    out["TimeUnit"] = (
        aws_sdk_cost_and_usage_report_service.types.time_unit.serialize_aws_json_1_1(
            value["time_unit"]
        )
    )
    import aws_sdk_cost_and_usage_report_service.types.report_format

    out["Format"] = (
        aws_sdk_cost_and_usage_report_service.types.report_format.serialize_aws_json_1_1(
            value["format"]
        )
    )
    import aws_sdk_cost_and_usage_report_service.types.compression_format

    out["Compression"] = (
        aws_sdk_cost_and_usage_report_service.types.compression_format.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    import aws_sdk_cost_and_usage_report_service.types.schema_element_list

    out["AdditionalSchemaElements"] = (
        aws_sdk_cost_and_usage_report_service.types.schema_element_list.serialize_aws_json_1_1(
            value["additional_schema_elements"]
        )
    )
    out["S3Bucket"] = value["s3_bucket"]
    out["S3Prefix"] = value["s3_prefix"]
    import aws_sdk_cost_and_usage_report_service.types.aws_region

    out["S3Region"] = (
        aws_sdk_cost_and_usage_report_service.types.aws_region.serialize_aws_json_1_1(
            value["s3_region"]
        )
    )
    if "additional_artifacts" in value:
        import aws_sdk_cost_and_usage_report_service.types.additional_artifact_list

        out["AdditionalArtifacts"] = (
            aws_sdk_cost_and_usage_report_service.types.additional_artifact_list.serialize_aws_json_1_1(
                value["additional_artifacts"]
            )
        )
    if "refresh_closed_reports" in value:
        out["RefreshClosedReports"] = value["refresh_closed_reports"]
    if "report_versioning" in value:
        import aws_sdk_cost_and_usage_report_service.types.report_versioning

        out["ReportVersioning"] = (
            aws_sdk_cost_and_usage_report_service.types.report_versioning.serialize_aws_json_1_1(
                value["report_versioning"]
            )
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "report_status" in value:
        import aws_sdk_cost_and_usage_report_service.types.report_status

        out["ReportStatus"] = (
            aws_sdk_cost_and_usage_report_service.types.report_status.serialize_aws_json_1_1(
                value["report_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportDefinition:
    out: ReportDefinition = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    else:
        raise DeserializationError("ReportDefinition.report_name required")
    if "TimeUnit" in data:
        import aws_sdk_cost_and_usage_report_service.types.time_unit

        out["time_unit"] = (
            aws_sdk_cost_and_usage_report_service.types.time_unit.deserialize_aws_json_1_1(
                data["TimeUnit"]
            )
        )
    else:
        raise DeserializationError("ReportDefinition.time_unit required")
    if "Format" in data:
        import aws_sdk_cost_and_usage_report_service.types.report_format

        out["format"] = (
            aws_sdk_cost_and_usage_report_service.types.report_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    else:
        raise DeserializationError("ReportDefinition.format required")
    if "Compression" in data:
        import aws_sdk_cost_and_usage_report_service.types.compression_format

        out["compression"] = (
            aws_sdk_cost_and_usage_report_service.types.compression_format.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        raise DeserializationError("ReportDefinition.compression required")
    if "AdditionalSchemaElements" in data:
        import aws_sdk_cost_and_usage_report_service.types.schema_element_list

        out["additional_schema_elements"] = (
            aws_sdk_cost_and_usage_report_service.types.schema_element_list.deserialize_aws_json_1_1(
                data["AdditionalSchemaElements"]
            )
        )
    else:
        raise DeserializationError(
            "ReportDefinition.additional_schema_elements required"
        )
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("ReportDefinition.s3_bucket required")
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    else:
        raise DeserializationError("ReportDefinition.s3_prefix required")
    if "S3Region" in data:
        import aws_sdk_cost_and_usage_report_service.types.aws_region

        out["s3_region"] = (
            aws_sdk_cost_and_usage_report_service.types.aws_region.deserialize_aws_json_1_1(
                data["S3Region"]
            )
        )
    else:
        raise DeserializationError("ReportDefinition.s3_region required")
    if "AdditionalArtifacts" in data:
        import aws_sdk_cost_and_usage_report_service.types.additional_artifact_list

        out["additional_artifacts"] = (
            aws_sdk_cost_and_usage_report_service.types.additional_artifact_list.deserialize_aws_json_1_1(
                data["AdditionalArtifacts"]
            )
        )
    if "RefreshClosedReports" in data:
        out["refresh_closed_reports"] = data["RefreshClosedReports"]
    if "ReportVersioning" in data:
        import aws_sdk_cost_and_usage_report_service.types.report_versioning

        out["report_versioning"] = (
            aws_sdk_cost_and_usage_report_service.types.report_versioning.deserialize_aws_json_1_1(
                data["ReportVersioning"]
            )
        )
    if "BillingViewArn" in data:
        out["billing_view_arn"] = data["BillingViewArn"]
    if "ReportStatus" in data:
        import aws_sdk_cost_and_usage_report_service.types.report_status

        out["report_status"] = (
            aws_sdk_cost_and_usage_report_service.types.report_status.deserialize_aws_json_1_1(
                data["ReportStatus"]
            )
        )
    return out
