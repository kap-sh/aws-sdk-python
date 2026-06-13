"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_error_type
    import aws_sdk_quicksight.types.entity_list
    import aws_sdk_quicksight.types.non_empty_string


class AnalysisError(TypedDict):
    type: NotRequired["aws_sdk_quicksight.types.analysis_error_type.AnalysisErrorType"]
    """<p>The type of the analysis error.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The message associated with the analysis error.</p>"""
    violated_entities: NotRequired["aws_sdk_quicksight.types.entity_list.EntityList"]
    """<p>Lists the violated entities that caused the analysis error</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisError) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_quicksight.types.analysis_error_type

        out["Type"] = aws_sdk_quicksight.types.analysis_error_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "violated_entities" in value:
        import aws_sdk_quicksight.types.entity_list

        out["ViolatedEntities"] = aws_sdk_quicksight.types.entity_list.serialize_json(
            value["violated_entities"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisError:
    out: AnalysisError = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_quicksight.types.analysis_error_type

        out["type"] = aws_sdk_quicksight.types.analysis_error_type.deserialize_json(
            data["Type"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ViolatedEntities" in data:
        import aws_sdk_quicksight.types.entity_list

        out["violated_entities"] = (
            aws_sdk_quicksight.types.entity_list.deserialize_json(
                data["ViolatedEntities"]
            )
        )
    return out
