"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PutRegistryCatalogDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.registry_display_name


class PutRegistryCatalogDataRequest(TypedDict, closed=True):
    display_name: NotRequired[
        "aws_sdk_ecr_public.types.registry_display_name.RegistryDisplayName"
    ]
    """<p>The display name for a public registry. The display name is shown as the repository author in the Amazon ECR Public Gallery.</p> <note> <p>The registry display name is only publicly visible in the Amazon ECR Public Gallery for verified accounts.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRegistryCatalogDataRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRegistryCatalogDataRequest:
    out: PutRegistryCatalogDataRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
