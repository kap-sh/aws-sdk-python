"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseManagerReportGeneratorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.client_request_token
    import aws_sdk_license_manager.types.report_context
    import aws_sdk_license_manager.types.report_frequency
    import aws_sdk_license_manager.types.report_generator_name
    import aws_sdk_license_manager.types.report_type_list
    import aws_sdk_license_manager.types.string


class UpdateLicenseManagerReportGeneratorRequest(TypedDict):
    license_manager_report_generator_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the report generator to update.</p>"""
    report_generator_name: (
        "aws_sdk_license_manager.types.report_generator_name.ReportGeneratorName"
    )
    """<p>Name of the report generator.</p>"""
    type: "aws_sdk_license_manager.types.report_type_list.ReportTypeList"
    """<p>Type of reports to generate. The following report types are supported:</p> <ul> <li> <p>License configuration report - Reports the number and details of consumed licenses for a license configuration.</p> </li> <li> <p>Resource report - Reports the tracked licenses and resource consumption for a license configuration.</p> </li> </ul>"""
    report_context: "aws_sdk_license_manager.types.report_context.ReportContext"
    """<p>The report context.</p>"""
    report_frequency: "aws_sdk_license_manager.types.report_frequency.ReportFrequency"
    """<p>Frequency by which reports are generated.</p>"""
    client_token: (
        "aws_sdk_license_manager.types.client_request_token.ClientRequestToken"
    )
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Description of the report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseManagerReportGeneratorRequest) -> dict:
    out: dict = {}
    out["LicenseManagerReportGeneratorArn"] = value[
        "license_manager_report_generator_arn"
    ]
    out["ReportGeneratorName"] = value["report_generator_name"]
    import aws_sdk_license_manager.types.report_type_list

    out["Type"] = aws_sdk_license_manager.types.report_type_list.serialize_aws_json_1_1(
        value["type"]
    )
    import aws_sdk_license_manager.types.report_context

    out["ReportContext"] = (
        aws_sdk_license_manager.types.report_context.serialize_aws_json_1_1(
            value["report_context"]
        )
    )
    import aws_sdk_license_manager.types.report_frequency

    out["ReportFrequency"] = (
        aws_sdk_license_manager.types.report_frequency.serialize_aws_json_1_1(
            value["report_frequency"]
        )
    )
    out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseManagerReportGeneratorRequest:
    out: UpdateLicenseManagerReportGeneratorRequest = {}  # type: ignore[typeddict-item]
    if "LicenseManagerReportGeneratorArn" in data:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.license_manager_report_generator_arn required"
        )
    if "ReportGeneratorName" in data:
        out["report_generator_name"] = data["ReportGeneratorName"]
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.report_generator_name required"
        )
    if "Type" in data:
        import aws_sdk_license_manager.types.report_type_list

        out["type"] = (
            aws_sdk_license_manager.types.report_type_list.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.type required"
        )
    if "ReportContext" in data:
        import aws_sdk_license_manager.types.report_context

        out["report_context"] = (
            aws_sdk_license_manager.types.report_context.deserialize_aws_json_1_1(
                data["ReportContext"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.report_context required"
        )
    if "ReportFrequency" in data:
        import aws_sdk_license_manager.types.report_frequency

        out["report_frequency"] = (
            aws_sdk_license_manager.types.report_frequency.deserialize_aws_json_1_1(
                data["ReportFrequency"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.report_frequency required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.client_token required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
