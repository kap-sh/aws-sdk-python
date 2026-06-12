"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseManagerReportGeneratorRequest``."""

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
    import aws_sdk_license_manager.types.tag_list


class CreateLicenseManagerReportGeneratorRequest(TypedDict):
    report_generator_name: (
        "aws_sdk_license_manager.types.report_generator_name.ReportGeneratorName"
    )
    """<p>Name of the report generator.</p>"""
    type: "aws_sdk_license_manager.types.report_type_list.ReportTypeList"
    """<p>Type of reports to generate. The following report types an be generated:</p> <ul> <li> <p>License configuration report - Reports the number and details of consumed licenses for a license configuration.</p> </li> <li> <p>Resource report - Reports the tracked licenses and resource consumption for a license configuration.</p> </li> </ul>"""
    report_context: "aws_sdk_license_manager.types.report_context.ReportContext"
    """<p>Defines the type of license configuration the report generator tracks.</p>"""
    report_frequency: "aws_sdk_license_manager.types.report_frequency.ReportFrequency"
    """<p>Frequency by which reports are generated. Reports can be generated daily, monthly, or weekly.</p>"""
    client_token: (
        "aws_sdk_license_manager.types.client_request_token.ClientRequestToken"
    )
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Description of the report generator.</p>"""
    tags: NotRequired["aws_sdk_license_manager.types.tag_list.TagList"]
    """<p>Tags to add to the report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseManagerReportGeneratorRequest) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import aws_sdk_license_manager.types.tag_list

        out["Tags"] = aws_sdk_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseManagerReportGeneratorRequest:
    out: CreateLicenseManagerReportGeneratorRequest = {}  # type: ignore[typeddict-item]
    if "ReportGeneratorName" in data:
        out["report_generator_name"] = data["ReportGeneratorName"]
    else:
        raise DeserializationError(
            "CreateLicenseManagerReportGeneratorRequest.report_generator_name required"
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
            "CreateLicenseManagerReportGeneratorRequest.type required"
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
            "CreateLicenseManagerReportGeneratorRequest.report_context required"
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
            "CreateLicenseManagerReportGeneratorRequest.report_frequency required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateLicenseManagerReportGeneratorRequest.client_token required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_license_manager.types.tag_list

        out["tags"] = aws_sdk_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
