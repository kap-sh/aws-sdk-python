"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseConversionTaskForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.license_conversion_context


class CreateLicenseConversionTaskForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the resource you are converting the license type for.</p>"""
    source_license_context: "aws_sdk_license_manager.types.license_conversion_context.LicenseConversionContext"
    r"""<p>Information that identifies the license type you are converting from. For the structure of the source license, see <a href=\"https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli\">Convert a license type using the CLI </a> in the <i>License Manager User Guide</i>.</p>"""
    destination_license_context: "aws_sdk_license_manager.types.license_conversion_context.LicenseConversionContext"
    r"""<p>Information that identifies the license type you are converting to. For the structure of the destination license, see <a href=\"https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli\">Convert a license type using the CLI </a> in the <i>License Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateLicenseConversionTaskForResourceRequest,
) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_license_manager.types.license_conversion_context

    out["SourceLicenseContext"] = (
        aws_sdk_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
            value["source_license_context"]
        )
    )
    import aws_sdk_license_manager.types.license_conversion_context

    out["DestinationLicenseContext"] = (
        aws_sdk_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
            value["destination_license_context"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateLicenseConversionTaskForResourceRequest:
    out: CreateLicenseConversionTaskForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "CreateLicenseConversionTaskForResourceRequest.resource_arn required"
        )
    if "SourceLicenseContext" in data:
        import aws_sdk_license_manager.types.license_conversion_context

        out["source_license_context"] = (
            aws_sdk_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["SourceLicenseContext"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseConversionTaskForResourceRequest.source_license_context required"
        )
    if "DestinationLicenseContext" in data:
        import aws_sdk_license_manager.types.license_conversion_context

        out["destination_license_context"] = (
            aws_sdk_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["DestinationLicenseContext"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseConversionTaskForResourceRequest.destination_license_context required"
        )
    return out
