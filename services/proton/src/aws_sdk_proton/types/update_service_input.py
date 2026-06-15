"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.spec_contents


class UpdateServiceInput(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service to edit.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>The edited service description.</p>"""
    spec: NotRequired["aws_sdk_proton.types.spec_contents.SpecContents"]
    r"""<p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html\">Edit a service</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "spec" in value:
        out["spec"] = value["spec"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceInput:
    out: UpdateServiceInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateServiceInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "spec" in data:
        out["spec"] = data["spec"]
    return out
