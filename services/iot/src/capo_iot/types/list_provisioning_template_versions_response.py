"""Generated from Smithy shape ``com.amazonaws.iot#ListProvisioningTemplateVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.provisioning_template_version_listing


class ListProvisioningTemplateVersionsResponse(TypedDict, closed=True):
    versions: NotRequired[
        "capo_iot.types.provisioning_template_version_listing.ProvisioningTemplateVersionListing"
    ]
    """<p>The list of provisioning template versions.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisioningTemplateVersionsResponse) -> dict:
    out: dict = {}
    if "versions" in value:
        import capo_iot.types.provisioning_template_version_listing

        out["versions"] = (
            capo_iot.types.provisioning_template_version_listing.serialize_json(
                value["versions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProvisioningTemplateVersionsResponse:
    out: ListProvisioningTemplateVersionsResponse = {}  # type: ignore[typeddict-item]
    if "versions" in data:
        import capo_iot.types.provisioning_template_version_listing

        out["versions"] = (
            capo_iot.types.provisioning_template_version_listing.deserialize_json(
                data["versions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
