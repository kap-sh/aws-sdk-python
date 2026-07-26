"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionsByCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.max_list_items
    import capo_lambda.types.string


class ListFunctionsByCodeSigningConfigRequest(TypedDict, closed=True):
    code_signing_config_arn: (
        "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["capo_lambda.types.max_list_items.MaxListItems"]
    """<p>Maximum number of items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsByCodeSigningConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionsByCodeSigningConfigRequest:
    out: ListFunctionsByCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    return out
