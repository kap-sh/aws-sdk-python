"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time_timestamp
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.image_pipeline_arn
    import aws_sdk_imagebuilder.types.inspector_score_details
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.non_negative_double
    import aws_sdk_imagebuilder.types.package_vulnerability_details
    import aws_sdk_imagebuilder.types.remediation


class ImageScanFinding(TypedDict):
    aws_account_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account ID that's associated with the finding.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image build version that's associated with the finding.</p>"""
    image_pipeline_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image pipeline that's associated with the finding.</p>"""
    type: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The type of the finding. Image Builder looks for findings of the type <code>PACKAGE_VULNERABILITY</code> that apply to output images, and excludes other types.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the finding.</p>"""
    title: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The title of the finding.</p>"""
    remediation: NotRequired["aws_sdk_imagebuilder.types.remediation.Remediation"]
    """<p>An object that contains the details about how to remediate the finding.</p>"""
    severity: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The severity of the finding.</p>"""
    first_observed_at: NotRequired[
        "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time when the finding was first observed.</p>"""
    updated_at: NotRequired[
        "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when the finding was last updated.</p>"""
    inspector_score: NotRequired[
        "aws_sdk_imagebuilder.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>The score that Amazon Inspector assigned for the finding.</p>"""
    inspector_score_details: NotRequired[
        "aws_sdk_imagebuilder.types.inspector_score_details.InspectorScoreDetails"
    ]
    """<p>An object that contains details of the Amazon Inspector score.</p>"""
    package_vulnerability_details: NotRequired[
        "aws_sdk_imagebuilder.types.package_vulnerability_details.PackageVulnerabilityDetails"
    ]
    """<p>An object that contains the details of a package vulnerability finding.</p>"""
    fix_available: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Details about whether a fix is available for any of the packages that are identified in the finding through a version update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFinding) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "image_pipeline_arn" in value:
        out["imagePipelineArn"] = value["image_pipeline_arn"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "title" in value:
        out["title"] = value["title"]
    if "remediation" in value:
        import aws_sdk_imagebuilder.types.remediation

        out["remediation"] = aws_sdk_imagebuilder.types.remediation.serialize_json(
            value["remediation"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "first_observed_at" in value:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["firstObservedAt"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.serialize_json(
                value["first_observed_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["updatedAt"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "inspector_score" in value:
        out["inspectorScore"] = value["inspector_score"]
    if "inspector_score_details" in value:
        import aws_sdk_imagebuilder.types.inspector_score_details

        out["inspectorScoreDetails"] = (
            aws_sdk_imagebuilder.types.inspector_score_details.serialize_json(
                value["inspector_score_details"]
            )
        )
    if "package_vulnerability_details" in value:
        import aws_sdk_imagebuilder.types.package_vulnerability_details

        out["packageVulnerabilityDetails"] = (
            aws_sdk_imagebuilder.types.package_vulnerability_details.serialize_json(
                value["package_vulnerability_details"]
            )
        )
    if "fix_available" in value:
        out["fixAvailable"] = value["fix_available"]
    return out


def deserialize_json(data: dict) -> ImageScanFinding:
    out: ImageScanFinding = {}  # type: ignore[typeddict-item]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "imagePipelineArn" in data:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    if "type" in data:
        out["type"] = data["type"]
    if "description" in data:
        out["description"] = data["description"]
    if "title" in data:
        out["title"] = data["title"]
    if "remediation" in data:
        import aws_sdk_imagebuilder.types.remediation

        out["remediation"] = aws_sdk_imagebuilder.types.remediation.deserialize_json(
            data["remediation"]
        )
    if "severity" in data:
        out["severity"] = data["severity"]
    if "firstObservedAt" in data:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["first_observed_at"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["firstObservedAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["updated_at"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "inspectorScore" in data:
        out["inspector_score"] = data["inspectorScore"]
    if "inspectorScoreDetails" in data:
        import aws_sdk_imagebuilder.types.inspector_score_details

        out["inspector_score_details"] = (
            aws_sdk_imagebuilder.types.inspector_score_details.deserialize_json(
                data["inspectorScoreDetails"]
            )
        )
    if "packageVulnerabilityDetails" in data:
        import aws_sdk_imagebuilder.types.package_vulnerability_details

        out["package_vulnerability_details"] = (
            aws_sdk_imagebuilder.types.package_vulnerability_details.deserialize_json(
                data["packageVulnerabilityDetails"]
            )
        )
    if "fixAvailable" in data:
        out["fix_available"] = data["fixAvailable"]
    return out
