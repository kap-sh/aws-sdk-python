"""Generated from Smithy shape ``com.amazonaws.sagemaker#RenderUiTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.rendering_error_list
    import capo_sagemaker.types.string


class RenderUiTemplateResponse(TypedDict, closed=True):
    rendered_content: NotRequired["capo_sagemaker.types.string.String"]
    """<p>A Liquid template that renders the HTML for the worker UI.</p>"""
    errors: NotRequired["capo_sagemaker.types.rendering_error_list.RenderingErrorList"]
    """<p>A list of one or more <code>RenderingError</code> objects if any were encountered while rendering the template. If there were no errors, the list is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenderUiTemplateResponse) -> dict:
    out: dict = {}
    if "rendered_content" in value:
        out["RenderedContent"] = value["rendered_content"]
    if "errors" in value:
        import capo_sagemaker.types.rendering_error_list

        out["Errors"] = (
            capo_sagemaker.types.rendering_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenderUiTemplateResponse:
    out: RenderUiTemplateResponse = {}  # type: ignore[typeddict-item]
    if "RenderedContent" in data:
        out["rendered_content"] = data["RenderedContent"]
    if "Errors" in data:
        import capo_sagemaker.types.rendering_error_list

        out["errors"] = (
            capo_sagemaker.types.rendering_error_list.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
