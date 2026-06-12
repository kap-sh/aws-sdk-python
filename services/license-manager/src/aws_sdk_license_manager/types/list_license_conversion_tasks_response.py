"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseConversionTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_conversion_tasks
    import aws_sdk_license_manager.types.string


class ListLicenseConversionTasksResponse(TypedDict):
    license_conversion_tasks: NotRequired[
        "aws_sdk_license_manager.types.license_conversion_tasks.LicenseConversionTasks"
    ]
    """<p>Information about the license configuration tasks for your account.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseConversionTasksResponse) -> dict:
    out: dict = {}
    if "license_conversion_tasks" in value:
        import aws_sdk_license_manager.types.license_conversion_tasks

        out["LicenseConversionTasks"] = (
            aws_sdk_license_manager.types.license_conversion_tasks.serialize_aws_json_1_1(
                value["license_conversion_tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseConversionTasksResponse:
    out: ListLicenseConversionTasksResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConversionTasks" in data:
        import aws_sdk_license_manager.types.license_conversion_tasks

        out["license_conversion_tasks"] = (
            aws_sdk_license_manager.types.license_conversion_tasks.deserialize_aws_json_1_1(
                data["LicenseConversionTasks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
