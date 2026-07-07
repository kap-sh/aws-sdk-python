"""Generated from Smithy shape ``com.amazonaws.lambda#StepSucceededDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_result
    import aws_sdk_lambda.types.retry_details


class StepSucceededDetails(TypedDict, closed=True):
    result: "aws_sdk_lambda.types.event_result.EventResult"
    """<p>The response payload from the successful operation.</p>"""
    retry_details: "aws_sdk_lambda.types.retry_details.RetryDetails"
    """<p>Information about retry attempts for this step operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepSucceededDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_result

    out["Result"] = aws_sdk_lambda.types.event_result.serialize_json(value["result"])
    import aws_sdk_lambda.types.retry_details

    out["RetryDetails"] = aws_sdk_lambda.types.retry_details.serialize_json(
        value["retry_details"]
    )
    return out


def deserialize_json(data: dict) -> StepSucceededDetails:
    out: StepSucceededDetails = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        import aws_sdk_lambda.types.event_result

        out["result"] = aws_sdk_lambda.types.event_result.deserialize_json(
            data["Result"]
        )
    else:
        raise DeserializationError("StepSucceededDetails.result required")
    if "RetryDetails" in data:
        import aws_sdk_lambda.types.retry_details

        out["retry_details"] = aws_sdk_lambda.types.retry_details.deserialize_json(
            data["RetryDetails"]
        )
    else:
        raise DeserializationError("StepSucceededDetails.retry_details required")
    return out
