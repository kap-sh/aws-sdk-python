"""Generated from Smithy shape ``com.amazonaws.dynamodb#FailureException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.exception_description
    import aws_sdk_dynamodb.types.exception_name


class FailureException(TypedDict):
    exception_name: NotRequired["aws_sdk_dynamodb.types.exception_name.ExceptionName"]
    """<p>Exception name.</p>"""
    exception_description: NotRequired[
        "aws_sdk_dynamodb.types.exception_description.ExceptionDescription"
    ]
    """<p>Description of the failure.</p>"""
