"""Generated from Smithy shape ``com.amazonaws.iot#ListProvisioningTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.provisioning_template_listing


class ListProvisioningTemplatesResponse(TypedDict, closed=True):
    templates: NotRequired[
        "aws_sdk_iot.types.provisioning_template_listing.ProvisioningTemplateListing"
    ]
    """<p>A list of provisioning templates</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisioningTemplatesResponse) -> dict:
    out: dict = {}
    if "templates" in value:
        import aws_sdk_iot.types.provisioning_template_listing

        out["templates"] = (
            aws_sdk_iot.types.provisioning_template_listing.serialize_json(
                value["templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProvisioningTemplatesResponse:
    out: ListProvisioningTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "templates" in data:
        import aws_sdk_iot.types.provisioning_template_listing

        out["templates"] = (
            aws_sdk_iot.types.provisioning_template_listing.deserialize_json(
                data["templates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
