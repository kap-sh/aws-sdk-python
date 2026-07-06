"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentTemplateVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_template_version_summary_list
    import aws_sdk_proton.types.next_token


class ListEnvironmentTemplateVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next major or minor version in the array of major or minor versions of an environment template, after the list of major or minor versions that was previously requested.</p>"""
    template_versions: "aws_sdk_proton.types.environment_template_version_summary_list.EnvironmentTemplateVersionSummaryList"
    """<p>An array of major or minor versions of an environment template detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentTemplateVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.environment_template_version_summary_list

    out["templateVersions"] = (
        aws_sdk_proton.types.environment_template_version_summary_list.serialize_aws_json_1_0(
            value["template_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentTemplateVersionsOutput:
    out: ListEnvironmentTemplateVersionsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "templateVersions" in data:
        import aws_sdk_proton.types.environment_template_version_summary_list

        out["template_versions"] = (
            aws_sdk_proton.types.environment_template_version_summary_list.deserialize_aws_json_1_0(
                data["templateVersions"]
            )
        )
    else:
        raise DeserializationError(
            "ListEnvironmentTemplateVersionsOutput.template_versions required"
        )
    return out
