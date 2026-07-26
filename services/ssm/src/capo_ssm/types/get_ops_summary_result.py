"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsSummaryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.ops_entity_list


class GetOpsSummaryResult(TypedDict, closed=True):
    entities: NotRequired["capo_ssm.types.ops_entity_list.OpsEntityList"]
    """<p>The list of aggregated details and filtered OpsData.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsSummaryResult) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_ssm.types.ops_entity_list

        out["Entities"] = capo_ssm.types.ops_entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsSummaryResult:
    out: GetOpsSummaryResult = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import capo_ssm.types.ops_entity_list

        out["entities"] = capo_ssm.types.ops_entity_list.deserialize_aws_json_1_1(
            data["Entities"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
