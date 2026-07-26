"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListFailuresForLicenseConfigurationOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_operation_failure_list
    import capo_license_manager.types.string


class ListFailuresForLicenseConfigurationOperationsResponse(TypedDict, closed=True):
    license_operation_failure_list: NotRequired[
        "capo_license_manager.types.license_operation_failure_list.LicenseOperationFailureList"
    ]
    """<p>License configuration operations that failed.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListFailuresForLicenseConfigurationOperationsResponse,
) -> dict:
    out: dict = {}
    if "license_operation_failure_list" in value:
        import capo_license_manager.types.license_operation_failure_list

        out["LicenseOperationFailureList"] = (
            capo_license_manager.types.license_operation_failure_list.serialize_aws_json_1_1(
                value["license_operation_failure_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListFailuresForLicenseConfigurationOperationsResponse:
    out: ListFailuresForLicenseConfigurationOperationsResponse = {}  # type: ignore[typeddict-item]
    if "LicenseOperationFailureList" in data:
        import capo_license_manager.types.license_operation_failure_list

        out["license_operation_failure_list"] = (
            capo_license_manager.types.license_operation_failure_list.deserialize_aws_json_1_1(
                data["LicenseOperationFailureList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
