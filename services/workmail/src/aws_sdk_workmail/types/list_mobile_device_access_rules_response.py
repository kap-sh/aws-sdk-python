"""Generated from Smithy shape ``com.amazonaws.workmail#ListMobileDeviceAccessRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mobile_device_access_rules_list


class ListMobileDeviceAccessRulesResponse(TypedDict):
    rules: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rules_list.MobileDeviceAccessRulesList"
    ]
    """<p>The list of mobile device access rules that exist under the specified WorkMail organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMobileDeviceAccessRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_workmail.types.mobile_device_access_rules_list

        out["Rules"] = (
            aws_sdk_workmail.types.mobile_device_access_rules_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMobileDeviceAccessRulesResponse:
    out: ListMobileDeviceAccessRulesResponse = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_workmail.types.mobile_device_access_rules_list

        out["rules"] = (
            aws_sdk_workmail.types.mobile_device_access_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    return out
