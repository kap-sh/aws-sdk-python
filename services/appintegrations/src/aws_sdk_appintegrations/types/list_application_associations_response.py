"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListApplicationAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_associations_list
    import aws_sdk_appintegrations.types.next_token

class ListApplicationAssociationsResponse(TypedDict):
    application_associations: NotRequired["aws_sdk_appintegrations.types.application_associations_list.ApplicationAssociationsList"]
    """<p>List of Application Associations for the Application.</p>"""
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationAssociationsResponse) -> dict:
    out: dict = {}
    if "application_associations" in value:
        import aws_sdk_appintegrations.types.application_associations_list
        out["ApplicationAssociations"] = aws_sdk_appintegrations.types.application_associations_list.serialize_json(value["application_associations"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationAssociationsResponse:
    out: ListApplicationAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationAssociations" in data:
        import aws_sdk_appintegrations.types.application_associations_list
        out["application_associations"] = aws_sdk_appintegrations.types.application_associations_list.deserialize_json(data["ApplicationAssociations"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out