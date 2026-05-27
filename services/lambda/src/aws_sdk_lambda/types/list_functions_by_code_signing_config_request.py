"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionsByCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_config_arn
    import aws_sdk_lambda.types.max_list_items
    import aws_sdk_lambda.types.string


class ListFunctionsByCodeSigningConfigRequest(TypedDict):
    code_signing_config_arn: (
        "aws_sdk_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""
    marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["aws_sdk_lambda.types.max_list_items.MaxListItems"]
    """<p>Maximum number of items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsByCodeSigningConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionsByCodeSigningConfigRequest:
    out: ListFunctionsByCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    return out
