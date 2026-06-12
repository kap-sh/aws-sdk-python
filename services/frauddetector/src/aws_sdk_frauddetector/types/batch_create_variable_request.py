"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchCreateVariableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.tag_list
    import aws_sdk_frauddetector.types.variable_entry_list


class BatchCreateVariableRequest(TypedDict):
    variable_entries: (
        "aws_sdk_frauddetector.types.variable_entry_list.VariableEntryList"
    )
    """<p>The list of variables for the batch create variable request.</p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateVariableRequest) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.variable_entry_list

    out["variableEntries"] = (
        aws_sdk_frauddetector.types.variable_entry_list.serialize_aws_json_1_1(
            value["variable_entries"]
        )
    )
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreateVariableRequest:
    out: BatchCreateVariableRequest = {}  # type: ignore[typeddict-item]
    if "variableEntries" in data:
        import aws_sdk_frauddetector.types.variable_entry_list

        out["variable_entries"] = (
            aws_sdk_frauddetector.types.variable_entry_list.deserialize_aws_json_1_1(
                data["variableEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateVariableRequest.variable_entries required"
        )
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
