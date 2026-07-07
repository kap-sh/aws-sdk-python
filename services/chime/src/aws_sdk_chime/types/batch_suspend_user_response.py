"""Generated from Smithy shape ``com.amazonaws.chime#BatchSuspendUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.user_error_list


class BatchSuspendUserResponse(TypedDict, closed=True):
    user_errors: NotRequired["aws_sdk_chime.types.user_error_list.UserErrorList"]
    """<p>If the <a>BatchSuspendUser</a> action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSuspendUserResponse) -> dict:
    out: dict = {}
    if "user_errors" in value:
        import aws_sdk_chime.types.user_error_list

        out["UserErrors"] = aws_sdk_chime.types.user_error_list.serialize_json(
            value["user_errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchSuspendUserResponse:
    out: BatchSuspendUserResponse = {}  # type: ignore[typeddict-item]
    if "UserErrors" in data:
        import aws_sdk_chime.types.user_error_list

        out["user_errors"] = aws_sdk_chime.types.user_error_list.deserialize_json(
            data["UserErrors"]
        )
    return out
