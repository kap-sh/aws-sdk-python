"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchPutFieldOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_option_error_list


class BatchPutFieldOptionsResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_connectcases.types.field_option_error_list.FieldOptionErrorList"
    ]
    """<p>A list of field errors. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutFieldOptionsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_connectcases.types.field_option_error_list

        out["errors"] = (
            aws_sdk_connectcases.types.field_option_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutFieldOptionsResponse:
    out: BatchPutFieldOptionsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_connectcases.types.field_option_error_list

        out["errors"] = (
            aws_sdk_connectcases.types.field_option_error_list.deserialize_json(
                data["errors"]
            )
        )
    return out
