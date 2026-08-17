"""Generated from Smithy shape ``com.amazonaws.dynamodb#FailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.exception_description
    import capo_dynamodb.types.exception_name


class FailureException(TypedDict, closed=True):
    exception_name: NotRequired["capo_dynamodb.types.exception_name.ExceptionName"]
    """<p>Exception name.</p>"""
    exception_description: NotRequired[
        "capo_dynamodb.types.exception_description.ExceptionDescription"
    ]
    """<p>Description of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailureException) -> dict:
    out: dict = {}
    if "exception_name" in value:
        out["ExceptionName"] = value["exception_name"]
    if "exception_description" in value:
        out["ExceptionDescription"] = value["exception_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FailureException:
    out: FailureException = {}  # type: ignore[typeddict-item]
    if data.get("ExceptionName") is not None:
        out["exception_name"] = data["ExceptionName"]
    if data.get("ExceptionDescription") is not None:
        out["exception_description"] = data["ExceptionDescription"]
    return out
