"""Generated from Smithy shape ``com.amazonaws.workmail#ListAccessControlRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_control_rules_list


class ListAccessControlRulesResponse(TypedDict):
    rules: NotRequired[
        "aws_sdk_workmail.types.access_control_rules_list.AccessControlRulesList"
    ]
    """<p>The access control rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessControlRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_workmail.types.access_control_rules_list

        out["Rules"] = (
            aws_sdk_workmail.types.access_control_rules_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessControlRulesResponse:
    out: ListAccessControlRulesResponse = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_workmail.types.access_control_rules_list

        out["rules"] = (
            aws_sdk_workmail.types.access_control_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    return out
