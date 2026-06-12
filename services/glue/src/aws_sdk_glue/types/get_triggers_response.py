"""Generated from Smithy shape ``com.amazonaws.glue#GetTriggersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.trigger_list


class GetTriggersResponse(TypedDict):
    triggers: NotRequired["aws_sdk_glue.types.trigger_list.TriggerList"]
    """<p>A list of triggers for the specified job.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all the requested triggers have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTriggersResponse) -> dict:
    out: dict = {}
    if "triggers" in value:
        import aws_sdk_glue.types.trigger_list

        out["Triggers"] = aws_sdk_glue.types.trigger_list.serialize_aws_json_1_1(
            value["triggers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTriggersResponse:
    out: GetTriggersResponse = {}  # type: ignore[typeddict-item]
    if "Triggers" in data:
        import aws_sdk_glue.types.trigger_list

        out["triggers"] = aws_sdk_glue.types.trigger_list.deserialize_aws_json_1_1(
            data["Triggers"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
