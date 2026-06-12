"""Generated from Smithy shape ``com.amazonaws.datapipeline#QueryObjectsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.boolean
    import aws_sdk_data_pipeline.types.id_list
    import aws_sdk_data_pipeline.types.string


class QueryObjectsOutput(TypedDict):
    ids: NotRequired["aws_sdk_data_pipeline.types.id_list.idList"]
    """<p>The identifiers that match the query selectors.</p>"""
    marker: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>The starting point for the next page of results. To view the next page of results, call <code>QueryObjects</code> again with this marker value. If the value is null, there are no more results.</p>"""
    has_more_results: "aws_sdk_data_pipeline.types.boolean.boolean"
    """<p>Indicates whether there are more results that can be obtained by a subsequent call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryObjectsOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_data_pipeline.types.id_list

        out["ids"] = aws_sdk_data_pipeline.types.id_list.serialize_aws_json_1_1(
            value["ids"]
        )
    if "marker" in value:
        out["marker"] = value["marker"]
    out["hasMoreResults"] = value.get("has_more_results", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryObjectsOutput:
    out: QueryObjectsOutput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_data_pipeline.types.id_list

        out["ids"] = aws_sdk_data_pipeline.types.id_list.deserialize_aws_json_1_1(
            data["ids"]
        )
    if "marker" in data:
        out["marker"] = data["marker"]
    if "hasMoreResults" in data:
        out["has_more_results"] = data["hasMoreResults"]
    else:
        out["has_more_results"] = False
    return out
