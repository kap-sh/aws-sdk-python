"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceTemplateVersionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_version_part


class ListServiceTemplateVersionsInput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the list of major or minor versions that was previously requested.</p>"""
    max_results: NotRequired["aws_sdk_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of major or minor versions of a service template to list.</p>"""
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    major_version: NotRequired[
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>To view a list of minor of versions under a major version of a service template, include <code>major Version</code>.</p> <p>To view a list of major versions of a service template, <i>exclude</i> <code>major Version</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceTemplateVersionsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["templateName"] = value["template_name"]
    if "major_version" in value:
        out["majorVersion"] = value["major_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceTemplateVersionsInput:
    out: ListServiceTemplateVersionsInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "ListServiceTemplateVersionsInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    return out
