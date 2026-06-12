"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsSummaryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.ops_entity_list


class GetOpsSummaryResult(TypedDict):
    entities: NotRequired["aws_sdk_ssm.types.ops_entity_list.OpsEntityList"]
    """<p>The list of aggregated details and filtered OpsData.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsSummaryResult) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_ssm.types.ops_entity_list

        out["Entities"] = aws_sdk_ssm.types.ops_entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsSummaryResult:
    out: GetOpsSummaryResult = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_ssm.types.ops_entity_list

        out["entities"] = aws_sdk_ssm.types.ops_entity_list.deserialize_aws_json_1_1(
            data["Entities"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
