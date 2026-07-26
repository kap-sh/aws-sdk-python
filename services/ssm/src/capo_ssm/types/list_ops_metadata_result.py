"""Generated from Smithy shape ``com.amazonaws.ssm#ListOpsMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.ops_metadata_list


class ListOpsMetadataResult(TypedDict, closed=True):
    ops_metadata_list: NotRequired["capo_ssm.types.ops_metadata_list.OpsMetadataList"]
    """<p>Returns a list of OpsMetadata objects.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOpsMetadataResult) -> dict:
    out: dict = {}
    if "ops_metadata_list" in value:
        import capo_ssm.types.ops_metadata_list

        out["OpsMetadataList"] = (
            capo_ssm.types.ops_metadata_list.serialize_aws_json_1_1(
                value["ops_metadata_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOpsMetadataResult:
    out: ListOpsMetadataResult = {}  # type: ignore[typeddict-item]
    if "OpsMetadataList" in data:
        import capo_ssm.types.ops_metadata_list

        out["ops_metadata_list"] = (
            capo_ssm.types.ops_metadata_list.deserialize_aws_json_1_1(
                data["OpsMetadataList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
