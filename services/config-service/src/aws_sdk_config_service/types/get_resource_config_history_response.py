"""Generated from Smithy shape ``com.amazonaws.configservice#GetResourceConfigHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_item_list
    import aws_sdk_config_service.types.next_token


class GetResourceConfigHistoryResponse(TypedDict):
    configuration_items: NotRequired[
        "aws_sdk_config_service.types.configuration_item_list.ConfigurationItemList"
    ]
    """<p>An array of <code>ConfigurationItems</code> Objects. Contatins the configuration history for one or more resources.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceConfigHistoryResponse) -> dict:
    out: dict = {}
    if "configuration_items" in value:
        import aws_sdk_config_service.types.configuration_item_list

        out["configurationItems"] = (
            aws_sdk_config_service.types.configuration_item_list.serialize_aws_json_1_1(
                value["configuration_items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceConfigHistoryResponse:
    out: GetResourceConfigHistoryResponse = {}  # type: ignore[typeddict-item]
    if "configurationItems" in data:
        import aws_sdk_config_service.types.configuration_item_list

        out["configuration_items"] = (
            aws_sdk_config_service.types.configuration_item_list.deserialize_aws_json_1_1(
                data["configurationItems"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
