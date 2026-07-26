"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.client_id


class ApplicationAssociationSummary(TypedDict, closed=True):
    application_association_arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Application Association.</p>"""
    application_arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    client_id: NotRequired["capo_appintegrations.types.client_id.ClientId"]
    """<p>The identifier for the client that is associated with the Application Association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationAssociationSummary) -> dict:
    out: dict = {}
    if "application_association_arn" in value:
        out["ApplicationAssociationArn"] = value["application_association_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> ApplicationAssociationSummary:
    out: ApplicationAssociationSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationAssociationArn" in data:
        out["application_association_arn"] = data["ApplicationAssociationArn"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    return out
