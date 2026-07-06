"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetGraphMemberDatasourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id_extended_list
    import aws_sdk_detective.types.graph_arn


class BatchGetGraphMemberDatasourcesRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    account_ids: (
        "aws_sdk_detective.types.account_id_extended_list.AccountIdExtendedList"
    )
    """<p>The list of Amazon Web Services accounts to get data source package information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetGraphMemberDatasourcesRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import aws_sdk_detective.types.account_id_extended_list

    out["AccountIds"] = aws_sdk_detective.types.account_id_extended_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetGraphMemberDatasourcesRequest:
    out: BatchGetGraphMemberDatasourcesRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError(
            "BatchGetGraphMemberDatasourcesRequest.graph_arn required"
        )
    if "AccountIds" in data:
        import aws_sdk_detective.types.account_id_extended_list

        out["account_ids"] = (
            aws_sdk_detective.types.account_id_extended_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetGraphMemberDatasourcesRequest.account_ids required"
        )
    return out
