"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDefaultQBusinessApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.namespace


class UpdateDefaultQBusinessApplicationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Quick Sight account that is connected to the Amazon Q Business application that you want to update.</p>"""
    namespace: NotRequired["aws_sdk_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that contains the linked Amazon Q Business application. If this field is left blank, the default namespace is used. Currently, the default namespace is the only valid value for this parameter.</p>"""
    application_id: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The ID of the Amazon Q Business application that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDefaultQBusinessApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> UpdateDefaultQBusinessApplicationRequest:
    out: UpdateDefaultQBusinessApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "UpdateDefaultQBusinessApplicationRequest.application_id required"
        )
    return out
