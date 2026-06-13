"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.next_token
    import aws_sdk_pca_connector_ad.types.template_list


class ListTemplatesResponse(TypedDict):
    templates: NotRequired["aws_sdk_pca_connector_ad.types.template_list.TemplateList"]
    """<p>Custom configuration templates used when issuing a certificate. </p>"""
    next_token: NotRequired["aws_sdk_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesResponse) -> dict:
    out: dict = {}
    if "templates" in value:
        import aws_sdk_pca_connector_ad.types.template_list

        out["Templates"] = aws_sdk_pca_connector_ad.types.template_list.serialize_json(
            value["templates"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplatesResponse:
    out: ListTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "Templates" in data:
        import aws_sdk_pca_connector_ad.types.template_list

        out["templates"] = (
            aws_sdk_pca_connector_ad.types.template_list.deserialize_json(
                data["Templates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
