"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceErrorMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_error_type


class DataSourceErrorMessage(TypedDict):
    error_type: "aws_sdk_datazone.types.data_source_error_type.DataSourceErrorType"
    """<p>The type of the error message that is returned if the operation cannot be successfully completed.</p>"""
    error_detail: NotRequired["str"]
    """<p>The details of the error message that is returned if the operation cannot be successfully completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceErrorMessage) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.data_source_error_type

    out["errorType"] = aws_sdk_datazone.types.data_source_error_type.serialize_json(
        value["error_type"]
    )
    if "error_detail" in value:
        out["errorDetail"] = value["error_detail"]
    return out


def deserialize_json(data: dict) -> DataSourceErrorMessage:
    out: DataSourceErrorMessage = {}  # type: ignore[typeddict-item]
    if "errorType" in data:
        import aws_sdk_datazone.types.data_source_error_type

        out["error_type"] = (
            aws_sdk_datazone.types.data_source_error_type.deserialize_json(
                data["errorType"]
            )
        )
    else:
        raise DeserializationError("DataSourceErrorMessage.error_type required")
    if "errorDetail" in data:
        out["error_detail"] = data["errorDetail"]
    return out
