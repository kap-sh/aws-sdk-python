"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppLicenseUsageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.admin_app_license_usage_list
    import aws_sdk_appstream.types.string


class DescribeAppLicenseUsageResult(TypedDict):
    app_license_usages: NotRequired[
        "aws_sdk_appstream.types.admin_app_license_usage_list.AdminAppLicenseUsageList"
    ]
    """<p>Collection of license usage records.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>Token for pagination of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppLicenseUsageResult) -> dict:
    out: dict = {}
    if "app_license_usages" in value:
        import aws_sdk_appstream.types.admin_app_license_usage_list

        out["AppLicenseUsages"] = (
            aws_sdk_appstream.types.admin_app_license_usage_list.serialize_aws_json_1_1(
                value["app_license_usages"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppLicenseUsageResult:
    out: DescribeAppLicenseUsageResult = {}  # type: ignore[typeddict-item]
    if "AppLicenseUsages" in data:
        import aws_sdk_appstream.types.admin_app_license_usage_list

        out["app_license_usages"] = (
            aws_sdk_appstream.types.admin_app_license_usage_list.deserialize_aws_json_1_1(
                data["AppLicenseUsages"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
