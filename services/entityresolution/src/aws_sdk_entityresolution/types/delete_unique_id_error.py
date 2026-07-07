"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.delete_unique_id_error_type
    import aws_sdk_entityresolution.types.header_safe_unique_id


class DeleteUniqueIdError(TypedDict, closed=True):
    unique_id: "aws_sdk_entityresolution.types.header_safe_unique_id.HeaderSafeUniqueId"
    """<p>The unique ID that couldn't be deleted.</p>"""
    error_type: "aws_sdk_entityresolution.types.delete_unique_id_error_type.DeleteUniqueIdErrorType"
    """<p> The error type for the delete unique ID operation.</p> <p>The <code>SERVICE_ERROR</code> value indicates that an internal service-side problem occurred during the deletion operation.</p> <p>The <code>VALIDATION_ERROR</code> value indicates that the deletion operation couldn't complete because of invalid input parameters or data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUniqueIdError) -> dict:
    out: dict = {}
    out["uniqueId"] = value["unique_id"]
    import aws_sdk_entityresolution.types.delete_unique_id_error_type

    out["errorType"] = (
        aws_sdk_entityresolution.types.delete_unique_id_error_type.serialize_json(
            value["error_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteUniqueIdError:
    out: DeleteUniqueIdError = {}  # type: ignore[typeddict-item]
    if "uniqueId" in data:
        out["unique_id"] = data["uniqueId"]
    else:
        raise DeserializationError("DeleteUniqueIdError.unique_id required")
    if "errorType" in data:
        import aws_sdk_entityresolution.types.delete_unique_id_error_type

        out["error_type"] = (
            aws_sdk_entityresolution.types.delete_unique_id_error_type.deserialize_json(
                data["errorType"]
            )
        )
    else:
        raise DeserializationError("DeleteUniqueIdError.error_type required")
    return out
