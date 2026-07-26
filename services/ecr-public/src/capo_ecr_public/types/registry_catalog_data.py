"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryCatalogData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.registry_display_name


class RegistryCatalogData(TypedDict, closed=True):
    display_name: NotRequired[
        "capo_ecr_public.types.registry_display_name.RegistryDisplayName"
    ]
    """<p>The display name for a public registry. This appears on the Amazon ECR Public Gallery.</p> <important> <p>Only accounts that have the verified account badge can have a registry display name.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryCatalogData) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryCatalogData:
    out: RegistryCatalogData = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
