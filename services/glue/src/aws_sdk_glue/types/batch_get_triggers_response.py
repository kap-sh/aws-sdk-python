"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTriggersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.trigger_list
    import aws_sdk_glue.types.trigger_name_list


class BatchGetTriggersResponse(TypedDict, closed=True):
    triggers: NotRequired["aws_sdk_glue.types.trigger_list.TriggerList"]
    """<p>A list of trigger definitions.</p>"""
    triggers_not_found: NotRequired[
        "aws_sdk_glue.types.trigger_name_list.TriggerNameList"
    ]
    """<p>A list of names of triggers not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTriggersResponse) -> dict:
    out: dict = {}
    if "triggers" in value:
        import aws_sdk_glue.types.trigger_list

        out["Triggers"] = aws_sdk_glue.types.trigger_list.serialize_aws_json_1_1(
            value["triggers"]
        )
    if "triggers_not_found" in value:
        import aws_sdk_glue.types.trigger_name_list

        out["TriggersNotFound"] = (
            aws_sdk_glue.types.trigger_name_list.serialize_aws_json_1_1(
                value["triggers_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetTriggersResponse:
    out: BatchGetTriggersResponse = {}  # type: ignore[typeddict-item]
    if "Triggers" in data:
        import aws_sdk_glue.types.trigger_list

        out["triggers"] = aws_sdk_glue.types.trigger_list.deserialize_aws_json_1_1(
            data["Triggers"]
        )
    if "TriggersNotFound" in data:
        import aws_sdk_glue.types.trigger_name_list

        out["triggers_not_found"] = (
            aws_sdk_glue.types.trigger_name_list.deserialize_aws_json_1_1(
                data["TriggersNotFound"]
            )
        )
    return out
