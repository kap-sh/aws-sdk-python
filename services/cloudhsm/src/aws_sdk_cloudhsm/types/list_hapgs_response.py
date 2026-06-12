"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListHapgsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hapg_list
    import aws_sdk_cloudhsm.types.pagination_token


class ListHapgsResponse(TypedDict):
    hapg_list: "aws_sdk_cloudhsm.types.hapg_list.HapgList"
    """<p>The list of high-availability partition groups.</p>"""
    next_token: NotRequired["aws_sdk_cloudhsm.types.pagination_token.PaginationToken"]
    """<p>If not null, more results are available. Pass this value to <code>ListHapgs</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHapgsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cloudhsm.types.hapg_list

    out["HapgList"] = aws_sdk_cloudhsm.types.hapg_list.serialize_aws_json_1_1(
        value["hapg_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHapgsResponse:
    out: ListHapgsResponse = {}  # type: ignore[typeddict-item]
    if "HapgList" in data:
        import aws_sdk_cloudhsm.types.hapg_list

        out["hapg_list"] = aws_sdk_cloudhsm.types.hapg_list.deserialize_aws_json_1_1(
            data["HapgList"]
        )
    else:
        raise DeserializationError("ListHapgsResponse.hapg_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
