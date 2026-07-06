"""Generated from Smithy shape ``com.amazonaws.lambda#ListLayerVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.architecture
    import aws_sdk_lambda.types.layer_name
    import aws_sdk_lambda.types.max_layer_list_items
    import aws_sdk_lambda.types.runtime
    import aws_sdk_lambda.types.string


class ListLayerVersionsRequest(TypedDict, closed=True):
    compatible_runtime: NotRequired["aws_sdk_lambda.types.runtime.Runtime"]
    r"""<p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>"""
    layer_name: "aws_sdk_lambda.types.layer_name.LayerName"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>A pagination token returned by a previous call.</p>"""
    max_items: NotRequired[
        "aws_sdk_lambda.types.max_layer_list_items.MaxLayerListItems"
    ]
    """<p>The maximum number of versions to return.</p>"""
    compatible_architecture: NotRequired[
        "aws_sdk_lambda.types.architecture.Architecture"
    ]
    r"""<p>The compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayerVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLayerVersionsRequest:
    out: ListLayerVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
