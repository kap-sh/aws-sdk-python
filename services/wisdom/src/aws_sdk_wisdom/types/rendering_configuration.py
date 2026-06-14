"""Generated from Smithy shape ``com.amazonaws.wisdom#RenderingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uri


class RenderingConfiguration(TypedDict):
    template_uri: NotRequired["aws_sdk_wisdom.types.uri.Uri"]
    r"""<p>A URI template containing exactly one variable in <code>${variableName} </code>format. This can only be set for <code>EXTERNAL</code> knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:</p> <ul> <li> <p>Salesforce: <code>Id</code>, <code>ArticleNumber</code>, <code>VersionNumber</code>, <code>Title</code>, <code>PublishStatus</code>, or <code>IsDeleted</code> </p> </li> <li> <p>ServiceNow: <code>number</code>, <code>short_description</code>, <code>sys_mod_count</code>, <code>workflow_state</code>, or <code>active</code> </p> </li> <li> <p>Zendesk: <code>id</code>, <code>title</code>, <code>updated_at</code>, or <code>draft</code> </p> </li> </ul> <p>The variable is replaced with the actual value for a piece of content when calling <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContent.html\">GetContent</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenderingConfiguration) -> dict:
    out: dict = {}
    if "template_uri" in value:
        out["templateUri"] = value["template_uri"]
    return out


def deserialize_json(data: dict) -> RenderingConfiguration:
    out: RenderingConfiguration = {}  # type: ignore[typeddict-item]
    if "templateUri" in data:
        out["template_uri"] = data["templateUri"]
    return out
