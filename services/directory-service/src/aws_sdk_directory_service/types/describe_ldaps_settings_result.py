"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeLDAPSSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.ldaps_settings_info
    import aws_sdk_directory_service.types.next_token


class DescribeLDAPSSettingsResult(TypedDict):
    ldaps_settings_info: NotRequired[
        "aws_sdk_directory_service.types.ldaps_settings_info.LDAPSSettingsInfo"
    ]
    """<p>Information about LDAP security for the specified directory, including status of enablement, state last updated date time, and the reason for the state.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>The next token used to retrieve the LDAPS settings if the number of setting types exceeds page limit and there is another page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLDAPSSettingsResult) -> dict:
    out: dict = {}
    if "ldaps_settings_info" in value:
        import aws_sdk_directory_service.types.ldaps_settings_info

        out["LDAPSSettingsInfo"] = (
            aws_sdk_directory_service.types.ldaps_settings_info.serialize_aws_json_1_1(
                value["ldaps_settings_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLDAPSSettingsResult:
    out: DescribeLDAPSSettingsResult = {}  # type: ignore[typeddict-item]
    if "LDAPSSettingsInfo" in data:
        import aws_sdk_directory_service.types.ldaps_settings_info

        out["ldaps_settings_info"] = (
            aws_sdk_directory_service.types.ldaps_settings_info.deserialize_aws_json_1_1(
                data["LDAPSSettingsInfo"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
