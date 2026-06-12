"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListLFTagExpressionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_expressions_list
    import aws_sdk_lakeformation.types.token


class ListLFTagExpressionsResponse(TypedDict):
    lf_tag_expressions: NotRequired[
        "aws_sdk_lakeformation.types.lf_tag_expressions_list.LFTagExpressionsList"
    ]
    """<p>Logical expressions composed of one more LF-Tag key-value pairs.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLFTagExpressionsResponse) -> dict:
    out: dict = {}
    if "lf_tag_expressions" in value:
        import aws_sdk_lakeformation.types.lf_tag_expressions_list

        out["LFTagExpressions"] = (
            aws_sdk_lakeformation.types.lf_tag_expressions_list.serialize_json(
                value["lf_tag_expressions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLFTagExpressionsResponse:
    out: ListLFTagExpressionsResponse = {}  # type: ignore[typeddict-item]
    if "LFTagExpressions" in data:
        import aws_sdk_lakeformation.types.lf_tag_expressions_list

        out["lf_tag_expressions"] = (
            aws_sdk_lakeformation.types.lf_tag_expressions_list.deserialize_json(
                data["LFTagExpressions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
