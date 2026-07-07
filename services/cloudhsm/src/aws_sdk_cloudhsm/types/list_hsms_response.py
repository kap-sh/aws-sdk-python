"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListHsmsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hsm_list
    import aws_sdk_cloudhsm.types.pagination_token


class ListHsmsResponse(TypedDict, closed=True):
    hsm_list: NotRequired["aws_sdk_cloudhsm.types.hsm_list.HsmList"]
    """<p>The list of ARNs that identify the HSMs.</p>"""
    next_token: NotRequired["aws_sdk_cloudhsm.types.pagination_token.PaginationToken"]
    """<p>If not null, more results are available. Pass this value to <code>ListHsms</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHsmsResponse) -> dict:
    out: dict = {}
    if "hsm_list" in value:
        import aws_sdk_cloudhsm.types.hsm_list

        out["HsmList"] = aws_sdk_cloudhsm.types.hsm_list.serialize_aws_json_1_1(
            value["hsm_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHsmsResponse:
    out: ListHsmsResponse = {}  # type: ignore[typeddict-item]
    if "HsmList" in data:
        import aws_sdk_cloudhsm.types.hsm_list

        out["hsm_list"] = aws_sdk_cloudhsm.types.hsm_list.deserialize_aws_json_1_1(
            data["HsmList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
