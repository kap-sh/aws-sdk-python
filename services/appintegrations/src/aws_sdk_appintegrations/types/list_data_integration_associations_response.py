"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListDataIntegrationAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.data_integration_associations_list
    import aws_sdk_appintegrations.types.next_token


class ListDataIntegrationAssociationsResponse(TypedDict, closed=True):
    data_integration_associations: NotRequired[
        "aws_sdk_appintegrations.types.data_integration_associations_list.DataIntegrationAssociationsList"
    ]
    """<p>The Amazon Resource Name (ARN) and unique ID of the DataIntegration association.</p>"""
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationAssociationsResponse) -> dict:
    out: dict = {}
    if "data_integration_associations" in value:
        import aws_sdk_appintegrations.types.data_integration_associations_list

        out["DataIntegrationAssociations"] = (
            aws_sdk_appintegrations.types.data_integration_associations_list.serialize_json(
                value["data_integration_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationAssociationsResponse:
    out: ListDataIntegrationAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "DataIntegrationAssociations" in data:
        import aws_sdk_appintegrations.types.data_integration_associations_list

        out["data_integration_associations"] = (
            aws_sdk_appintegrations.types.data_integration_associations_list.deserialize_json(
                data["DataIntegrationAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
