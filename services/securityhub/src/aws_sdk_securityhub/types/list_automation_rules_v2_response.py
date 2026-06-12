"""Generated from Smithy shape ``com.amazonaws.securityhub#ListAutomationRulesV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_metadata_list_v2
    import aws_sdk_securityhub.types.next_token


class ListAutomationRulesV2Response(TypedDict):
    rules: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_metadata_list_v2.AutomationRulesMetadataListV2"
    ]
    """<p>An array of automation rules.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomationRulesV2Response) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_securityhub.types.automation_rules_metadata_list_v2

        out["Rules"] = (
            aws_sdk_securityhub.types.automation_rules_metadata_list_v2.serialize_json(
                value["rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomationRulesV2Response:
    out: ListAutomationRulesV2Response = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_securityhub.types.automation_rules_metadata_list_v2

        out["rules"] = (
            aws_sdk_securityhub.types.automation_rules_metadata_list_v2.deserialize_json(
                data["Rules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
