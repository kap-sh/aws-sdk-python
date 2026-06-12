"""Generated from Smithy shape ``com.amazonaws.inspector#FailedItemDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.bool
    import aws_sdk_inspector.types.failed_item_error_code


class FailedItemDetails(TypedDict):
    failure_code: "aws_sdk_inspector.types.failed_item_error_code.FailedItemErrorCode"
    """<p>The status code of a failed item.</p>"""
    retryable: "aws_sdk_inspector.types.bool.Bool"
    """<p>Indicates whether you can immediately retry a request for this item for a specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedItemDetails) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.failed_item_error_code

    out["failureCode"] = (
        aws_sdk_inspector.types.failed_item_error_code.serialize_aws_json_1_1(
            value["failure_code"]
        )
    )
    out["retryable"] = value["retryable"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedItemDetails:
    out: FailedItemDetails = {}  # type: ignore[typeddict-item]
    if "failureCode" in data:
        import aws_sdk_inspector.types.failed_item_error_code

        out["failure_code"] = (
            aws_sdk_inspector.types.failed_item_error_code.deserialize_aws_json_1_1(
                data["failureCode"]
            )
        )
    else:
        raise DeserializationError("FailedItemDetails.failure_code required")
    if "retryable" in data:
        out["retryable"] = data["retryable"]
    else:
        raise DeserializationError("FailedItemDetails.retryable required")
    return out
