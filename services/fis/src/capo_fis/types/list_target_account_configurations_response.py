"""Generated from Smithy shape ``com.amazonaws.fis#ListTargetAccountConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.next_token
    import capo_fis.types.target_account_configuration_list


class ListTargetAccountConfigurationsResponse(TypedDict, closed=True):
    target_account_configurations: NotRequired[
        "capo_fis.types.target_account_configuration_list.TargetAccountConfigurationList"
    ]
    """<p>The target account configurations.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetAccountConfigurationsResponse) -> dict:
    out: dict = {}
    if "target_account_configurations" in value:
        import capo_fis.types.target_account_configuration_list

        out["targetAccountConfigurations"] = (
            capo_fis.types.target_account_configuration_list.serialize_json(
                value["target_account_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetAccountConfigurationsResponse:
    out: ListTargetAccountConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "targetAccountConfigurations" in data:
        import capo_fis.types.target_account_configuration_list

        out["target_account_configurations"] = (
            capo_fis.types.target_account_configuration_list.deserialize_json(
                data["targetAccountConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
