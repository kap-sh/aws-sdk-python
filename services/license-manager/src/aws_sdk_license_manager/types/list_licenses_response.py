"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicensesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_list
    import aws_sdk_license_manager.types.string


class ListLicensesResponse(TypedDict, closed=True):
    licenses: NotRequired["aws_sdk_license_manager.types.license_list.LicenseList"]
    """<p>License details.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicensesResponse) -> dict:
    out: dict = {}
    if "licenses" in value:
        import aws_sdk_license_manager.types.license_list

        out["Licenses"] = (
            aws_sdk_license_manager.types.license_list.serialize_aws_json_1_1(
                value["licenses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicensesResponse:
    out: ListLicensesResponse = {}  # type: ignore[typeddict-item]
    if "Licenses" in data:
        import aws_sdk_license_manager.types.license_list

        out["licenses"] = (
            aws_sdk_license_manager.types.license_list.deserialize_aws_json_1_1(
                data["Licenses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
