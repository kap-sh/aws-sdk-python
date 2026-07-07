"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStorageConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.storage_configuration_summary_list


class ListStorageConfigurationsResponse(TypedDict, closed=True):
    storage_configurations: "aws_sdk_ivs_realtime.types.storage_configuration_summary_list.StorageConfigurationSummaryList"
    """<p>List of the matching storage configurations.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more storage configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStorageConfigurationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.storage_configuration_summary_list

    out["storageConfigurations"] = (
        aws_sdk_ivs_realtime.types.storage_configuration_summary_list.serialize_json(
            value["storage_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStorageConfigurationsResponse:
    out: ListStorageConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "storageConfigurations" in data:
        import aws_sdk_ivs_realtime.types.storage_configuration_summary_list

        out["storage_configurations"] = (
            aws_sdk_ivs_realtime.types.storage_configuration_summary_list.deserialize_json(
                data["storageConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListStorageConfigurationsResponse.storage_configurations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
