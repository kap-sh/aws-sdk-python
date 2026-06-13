"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceTemplatesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.service_template_summary_list


class ListServiceTemplatesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service template in the array of service templates, after the current requested list of service templates.</p>"""
    templates: (
        "aws_sdk_proton.types.service_template_summary_list.ServiceTemplateSummaryList"
    )
    """<p>An array of service templates with detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.service_template_summary_list

    out["templates"] = (
        aws_sdk_proton.types.service_template_summary_list.serialize_aws_json_1_0(
            value["templates"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceTemplatesOutput:
    out: ListServiceTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "templates" in data:
        import aws_sdk_proton.types.service_template_summary_list

        out["templates"] = (
            aws_sdk_proton.types.service_template_summary_list.deserialize_aws_json_1_0(
                data["templates"]
            )
        )
    else:
        raise DeserializationError("ListServiceTemplatesOutput.templates required")
    return out
