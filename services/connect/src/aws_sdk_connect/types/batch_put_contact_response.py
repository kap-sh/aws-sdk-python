"""Generated from Smithy shape ``com.amazonaws.connect#BatchPutContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.failed_request_list
    import aws_sdk_connect.types.successful_request_list


class BatchPutContactResponse(TypedDict, closed=True):
    successful_request_list: NotRequired[
        "aws_sdk_connect.types.successful_request_list.SuccessfulRequestList"
    ]
    """<p>List of requests for which contact was successfully created.</p>"""
    failed_request_list: NotRequired[
        "aws_sdk_connect.types.failed_request_list.FailedRequestList"
    ]
    """<p>List of requests for which contact creation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutContactResponse) -> dict:
    out: dict = {}
    if "successful_request_list" in value:
        import aws_sdk_connect.types.successful_request_list

        out["SuccessfulRequestList"] = (
            aws_sdk_connect.types.successful_request_list.serialize_json(
                value["successful_request_list"]
            )
        )
    if "failed_request_list" in value:
        import aws_sdk_connect.types.failed_request_list

        out["FailedRequestList"] = (
            aws_sdk_connect.types.failed_request_list.serialize_json(
                value["failed_request_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutContactResponse:
    out: BatchPutContactResponse = {}  # type: ignore[typeddict-item]
    if "SuccessfulRequestList" in data:
        import aws_sdk_connect.types.successful_request_list

        out["successful_request_list"] = (
            aws_sdk_connect.types.successful_request_list.deserialize_json(
                data["SuccessfulRequestList"]
            )
        )
    if "FailedRequestList" in data:
        import aws_sdk_connect.types.failed_request_list

        out["failed_request_list"] = (
            aws_sdk_connect.types.failed_request_list.deserialize_json(
                data["FailedRequestList"]
            )
        )
    return out
