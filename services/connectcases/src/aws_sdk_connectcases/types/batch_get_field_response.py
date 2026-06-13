"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.batch_get_field_error_list
    import aws_sdk_connectcases.types.batch_get_field_list


class BatchGetFieldResponse(TypedDict):
    fields: "aws_sdk_connectcases.types.batch_get_field_list.BatchGetFieldList"
    """<p>A list of detailed field information. </p>"""
    errors: (
        "aws_sdk_connectcases.types.batch_get_field_error_list.BatchGetFieldErrorList"
    )
    """<p>A list of field errors. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldResponse) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.batch_get_field_list

    out["fields"] = aws_sdk_connectcases.types.batch_get_field_list.serialize_json(
        value["fields"]
    )
    import aws_sdk_connectcases.types.batch_get_field_error_list

    out["errors"] = (
        aws_sdk_connectcases.types.batch_get_field_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFieldResponse:
    out: BatchGetFieldResponse = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.batch_get_field_list

        out["fields"] = (
            aws_sdk_connectcases.types.batch_get_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("BatchGetFieldResponse.fields required")
    if "errors" in data:
        import aws_sdk_connectcases.types.batch_get_field_error_list

        out["errors"] = (
            aws_sdk_connectcases.types.batch_get_field_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetFieldResponse.errors required")
    return out
