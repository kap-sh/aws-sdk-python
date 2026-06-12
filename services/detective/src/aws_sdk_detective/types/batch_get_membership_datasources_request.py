"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetMembershipDatasourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn_list


class BatchGetMembershipDatasourcesRequest(TypedDict):
    graph_arns: "aws_sdk_detective.types.graph_arn_list.GraphArnList"
    """<p>The ARN of the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMembershipDatasourcesRequest) -> dict:
    out: dict = {}
    import aws_sdk_detective.types.graph_arn_list

    out["GraphArns"] = aws_sdk_detective.types.graph_arn_list.serialize_json(
        value["graph_arns"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetMembershipDatasourcesRequest:
    out: BatchGetMembershipDatasourcesRequest = {}  # type: ignore[typeddict-item]
    if "GraphArns" in data:
        import aws_sdk_detective.types.graph_arn_list

        out["graph_arns"] = aws_sdk_detective.types.graph_arn_list.deserialize_json(
            data["GraphArns"]
        )
    else:
        raise DeserializationError(
            "BatchGetMembershipDatasourcesRequest.graph_arns required"
        )
    return out
