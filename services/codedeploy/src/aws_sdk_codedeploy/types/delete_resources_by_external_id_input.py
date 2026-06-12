"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteResourcesByExternalIdInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.external_id


class DeleteResourcesByExternalIdInput(TypedDict):
    external_id: NotRequired["aws_sdk_codedeploy.types.external_id.ExternalId"]
    """<p>The unique ID of an external resource (for example, a CloudFormation stack ID) that is linked to one or more CodeDeploy resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcesByExternalIdInput) -> dict:
    out: dict = {}
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcesByExternalIdInput:
    out: DeleteResourcesByExternalIdInput = {}  # type: ignore[typeddict-item]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    return out
