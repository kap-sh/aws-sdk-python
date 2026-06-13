"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_template_filter_list
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token


class ListEnvironmentsInput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next environment in the array of environments, after the list of environments that was previously requested.</p>"""
    max_results: NotRequired["aws_sdk_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of environments to list.</p>"""
    environment_templates: NotRequired[
        "aws_sdk_proton.types.environment_template_filter_list.EnvironmentTemplateFilterList"
    ]
    """<p>An array of the versions of the environment template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "environment_templates" in value:
        import aws_sdk_proton.types.environment_template_filter_list

        out["environmentTemplates"] = (
            aws_sdk_proton.types.environment_template_filter_list.serialize_aws_json_1_0(
                value["environment_templates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentsInput:
    out: ListEnvironmentsInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "environmentTemplates" in data:
        import aws_sdk_proton.types.environment_template_filter_list

        out["environment_templates"] = (
            aws_sdk_proton.types.environment_template_filter_list.deserialize_aws_json_1_0(
                data["environmentTemplates"]
            )
        )
    return out
