"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListOperationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.next_token
    import aws_sdk_ssm_sap.types.operation_list


class ListOperationsOutput(TypedDict, closed=True):
    operations: NotRequired["aws_sdk_ssm_sap.types.operation_list.OperationList"]
    """<p>List of operations performed by AWS Systems Manager for SAP.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOperationsOutput) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_ssm_sap.types.operation_list

        out["Operations"] = aws_sdk_ssm_sap.types.operation_list.serialize_json(
            value["operations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOperationsOutput:
    out: ListOperationsOutput = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import aws_sdk_ssm_sap.types.operation_list

        out["operations"] = aws_sdk_ssm_sap.types.operation_list.deserialize_json(
            data["Operations"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
