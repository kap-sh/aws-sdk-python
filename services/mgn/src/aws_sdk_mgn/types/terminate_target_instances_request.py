"""Generated from Smithy shape ``com.amazonaws.mgn#TerminateTargetInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds


class TerminateTargetInstancesRequest(TypedDict):
    source_server_i_ds: "aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs"
    """<p>Terminate Target instance by Source Server IDs.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Terminate Target instance by Tags.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Terminate Target instance by Account ID</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateTargetInstancesRequest) -> dict:
    out: dict = {}
    import aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds

    out["sourceServerIDs"] = (
        aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds.serialize_json(
            value["source_server_i_ds"]
        )
    )
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> TerminateTargetInstancesRequest:
    out: TerminateTargetInstancesRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerIDs" in data:
        import aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds

        out["source_server_i_ds"] = (
            aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds.deserialize_json(
                data["sourceServerIDs"]
            )
        )
    else:
        raise DeserializationError(
            "TerminateTargetInstancesRequest.source_server_i_ds required"
        )
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
