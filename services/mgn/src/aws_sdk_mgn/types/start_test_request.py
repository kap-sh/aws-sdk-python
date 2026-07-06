"""Generated from Smithy shape ``com.amazonaws.mgn#StartTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.start_test_request_source_server_i_ds
    import aws_sdk_mgn.types.tags_map


class StartTestRequest(TypedDict, closed=True):
    source_server_i_ds: "aws_sdk_mgn.types.start_test_request_source_server_i_ds.StartTestRequestSourceServerIDs"
    """<p>Start Test for Source Server IDs.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Start Test by Tags.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Start Test for Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestRequest) -> dict:
    out: dict = {}
    import aws_sdk_mgn.types.start_test_request_source_server_i_ds

    out["sourceServerIDs"] = (
        aws_sdk_mgn.types.start_test_request_source_server_i_ds.serialize_json(
            value["source_server_i_ds"]
        )
    )
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> StartTestRequest:
    out: StartTestRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerIDs" in data:
        import aws_sdk_mgn.types.start_test_request_source_server_i_ds

        out["source_server_i_ds"] = (
            aws_sdk_mgn.types.start_test_request_source_server_i_ds.deserialize_json(
                data["sourceServerIDs"]
            )
        )
    else:
        raise DeserializationError("StartTestRequest.source_server_i_ds required")
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
