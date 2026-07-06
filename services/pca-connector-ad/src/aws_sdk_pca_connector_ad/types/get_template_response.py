"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.template


class GetTemplateResponse(TypedDict, closed=True):
    template: NotRequired["aws_sdk_pca_connector_ad.types.template.Template"]
    """<p>A certificate template that the connector uses to issue certificates from a private CA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateResponse) -> dict:
    out: dict = {}
    if "template" in value:
        import aws_sdk_pca_connector_ad.types.template

        out["Template"] = aws_sdk_pca_connector_ad.types.template.serialize_json(
            value["template"]
        )
    return out


def deserialize_json(data: dict) -> GetTemplateResponse:
    out: GetTemplateResponse = {}  # type: ignore[typeddict-item]
    if "Template" in data:
        import aws_sdk_pca_connector_ad.types.template

        out["template"] = aws_sdk_pca_connector_ad.types.template.deserialize_json(
            data["Template"]
        )
    return out
