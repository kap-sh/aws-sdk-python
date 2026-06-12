"""Generated from Smithy shape ``com.amazonaws.glue#ListTriggersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.trigger_name_list


class ListTriggersResponse(TypedDict):
    trigger_names: NotRequired["aws_sdk_glue.types.trigger_name_list.TriggerNameList"]
    """<p>The names of all triggers in the account, or the triggers with the specified tags.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if the returned list does not contain the last metric available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTriggersResponse) -> dict:
    out: dict = {}
    if "trigger_names" in value:
        import aws_sdk_glue.types.trigger_name_list

        out["TriggerNames"] = (
            aws_sdk_glue.types.trigger_name_list.serialize_aws_json_1_1(
                value["trigger_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTriggersResponse:
    out: ListTriggersResponse = {}  # type: ignore[typeddict-item]
    if "TriggerNames" in data:
        import aws_sdk_glue.types.trigger_name_list

        out["trigger_names"] = (
            aws_sdk_glue.types.trigger_name_list.deserialize_aws_json_1_1(
                data["TriggerNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
