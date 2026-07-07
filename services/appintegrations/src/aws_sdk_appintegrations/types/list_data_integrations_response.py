"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListDataIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.data_integrations_list
    import aws_sdk_appintegrations.types.next_token


class ListDataIntegrationsResponse(TypedDict, closed=True):
    data_integrations: NotRequired[
        "aws_sdk_appintegrations.types.data_integrations_list.DataIntegrationsList"
    ]
    """<p>The DataIntegrations associated with this account.</p>"""
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationsResponse) -> dict:
    out: dict = {}
    if "data_integrations" in value:
        import aws_sdk_appintegrations.types.data_integrations_list

        out["DataIntegrations"] = (
            aws_sdk_appintegrations.types.data_integrations_list.serialize_json(
                value["data_integrations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationsResponse:
    out: ListDataIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "DataIntegrations" in data:
        import aws_sdk_appintegrations.types.data_integrations_list

        out["data_integrations"] = (
            aws_sdk_appintegrations.types.data_integrations_list.deserialize_json(
                data["DataIntegrations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
