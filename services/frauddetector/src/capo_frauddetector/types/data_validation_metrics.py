"""Generated from Smithy shape ``com.amazonaws.frauddetector#DataValidationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.field_validation_message_list
    import capo_frauddetector.types.file_validation_message_list


class DataValidationMetrics(TypedDict, closed=True):
    file_level_messages: NotRequired[
        "capo_frauddetector.types.file_validation_message_list.fileValidationMessageList"
    ]
    """<p>The file-specific model training data validation messages.</p>"""
    field_level_messages: NotRequired[
        "capo_frauddetector.types.field_validation_message_list.fieldValidationMessageList"
    ]
    """<p>The field-specific model training validation messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataValidationMetrics) -> dict:
    out: dict = {}
    if "file_level_messages" in value:
        import capo_frauddetector.types.file_validation_message_list

        out["fileLevelMessages"] = (
            capo_frauddetector.types.file_validation_message_list.serialize_aws_json_1_1(
                value["file_level_messages"]
            )
        )
    if "field_level_messages" in value:
        import capo_frauddetector.types.field_validation_message_list

        out["fieldLevelMessages"] = (
            capo_frauddetector.types.field_validation_message_list.serialize_aws_json_1_1(
                value["field_level_messages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataValidationMetrics:
    out: DataValidationMetrics = {}  # type: ignore[typeddict-item]
    if "fileLevelMessages" in data:
        import capo_frauddetector.types.file_validation_message_list

        out["file_level_messages"] = (
            capo_frauddetector.types.file_validation_message_list.deserialize_aws_json_1_1(
                data["fileLevelMessages"]
            )
        )
    if "fieldLevelMessages" in data:
        import capo_frauddetector.types.field_validation_message_list

        out["field_level_messages"] = (
            capo_frauddetector.types.field_validation_message_list.deserialize_aws_json_1_1(
                data["fieldLevelMessages"]
            )
        )
    return out
