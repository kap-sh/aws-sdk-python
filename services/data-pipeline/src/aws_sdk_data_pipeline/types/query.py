"""Generated from Smithy shape ``com.amazonaws.datapipeline#Query``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.selector_list


class Query(TypedDict):
    selectors: NotRequired["aws_sdk_data_pipeline.types.selector_list.SelectorList"]
    """<p>List of selectors that define the query. An object must satisfy all of the selectors to match the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Query) -> dict:
    out: dict = {}
    if "selectors" in value:
        import aws_sdk_data_pipeline.types.selector_list

        out["selectors"] = (
            aws_sdk_data_pipeline.types.selector_list.serialize_aws_json_1_1(
                value["selectors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Query:
    out: Query = {}  # type: ignore[typeddict-item]
    if "selectors" in data:
        import aws_sdk_data_pipeline.types.selector_list

        out["selectors"] = (
            aws_sdk_data_pipeline.types.selector_list.deserialize_aws_json_1_1(
                data["selectors"]
            )
        )
    return out
