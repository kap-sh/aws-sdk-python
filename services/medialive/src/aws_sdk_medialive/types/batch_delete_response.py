"""Generated from Smithy shape ``com.amazonaws.medialive#BatchDeleteResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_batch_failed_result_model
    import aws_sdk_medialive.types.__list_of_batch_successful_result_model


class BatchDeleteResponse(TypedDict):
    failed: NotRequired[
        "aws_sdk_medialive.types.__list_of_batch_failed_result_model.__listOfBatchFailedResultModel"
    ]
    """List of failed operations"""
    successful: NotRequired[
        "aws_sdk_medialive.types.__list_of_batch_successful_result_model.__listOfBatchSuccessfulResultModel"
    ]
    """List of successful operations"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteResponse) -> dict:
    out: dict = {}
    if "failed" in value:
        import aws_sdk_medialive.types.__list_of_batch_failed_result_model

        out["failed"] = (
            aws_sdk_medialive.types.__list_of_batch_failed_result_model.serialize_json(
                value["failed"]
            )
        )
    if "successful" in value:
        import aws_sdk_medialive.types.__list_of_batch_successful_result_model

        out["successful"] = (
            aws_sdk_medialive.types.__list_of_batch_successful_result_model.serialize_json(
                value["successful"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteResponse:
    out: BatchDeleteResponse = {}  # type: ignore[typeddict-item]
    if "failed" in data:
        import aws_sdk_medialive.types.__list_of_batch_failed_result_model

        out["failed"] = (
            aws_sdk_medialive.types.__list_of_batch_failed_result_model.deserialize_json(
                data["failed"]
            )
        )
    if "successful" in data:
        import aws_sdk_medialive.types.__list_of_batch_successful_result_model

        out["successful"] = (
            aws_sdk_medialive.types.__list_of_batch_successful_result_model.deserialize_json(
                data["successful"]
            )
        )
    return out
