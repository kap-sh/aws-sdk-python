"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppTemplateLibraryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_library_templates_list
    import aws_sdk_socialmessaging.types.next_token


class ListWhatsAppTemplateLibraryOutput(TypedDict):
    meta_library_templates: NotRequired[
        "aws_sdk_socialmessaging.types.meta_library_templates_list.MetaLibraryTemplatesList"
    ]
    """<p>A list of templates from Meta's library.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppTemplateLibraryOutput) -> dict:
    out: dict = {}
    if "meta_library_templates" in value:
        import aws_sdk_socialmessaging.types.meta_library_templates_list

        out["metaLibraryTemplates"] = (
            aws_sdk_socialmessaging.types.meta_library_templates_list.serialize_json(
                value["meta_library_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWhatsAppTemplateLibraryOutput:
    out: ListWhatsAppTemplateLibraryOutput = {}  # type: ignore[typeddict-item]
    if "metaLibraryTemplates" in data:
        import aws_sdk_socialmessaging.types.meta_library_templates_list

        out["meta_library_templates"] = (
            aws_sdk_socialmessaging.types.meta_library_templates_list.deserialize_json(
                data["metaLibraryTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
