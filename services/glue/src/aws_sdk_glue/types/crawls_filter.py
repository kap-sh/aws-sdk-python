"""Generated from Smithy shape ``com.amazonaws.glue#CrawlsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.field_name
    import aws_sdk_glue.types.filter_operator
    import aws_sdk_glue.types.generic_string


class CrawlsFilter(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_glue.types.field_name.FieldName"]
    """<p>A key used to filter the crawler runs for a specified crawler. Valid values for each of the field names are:</p> <ul> <li> <p> <code>CRAWL_ID</code>: A string representing the UUID identifier for a crawl.</p> </li> <li> <p> <code>STATE</code>: A string representing the state of the crawl.</p> </li> <li> <p> <code>START_TIME</code> and <code>END_TIME</code>: The epoch timestamp in milliseconds.</p> </li> <li> <p> <code>DPU_HOUR</code>: The number of data processing unit (DPU) hours used for the crawl.</p> </li> </ul>"""
    filter_operator: NotRequired["aws_sdk_glue.types.filter_operator.FilterOperator"]
    """<p>A defined comparator that operates on the value. The available operators are:</p> <ul> <li> <p> <code>GT</code>: Greater than.</p> </li> <li> <p> <code>GE</code>: Greater than or equal to.</p> </li> <li> <p> <code>LT</code>: Less than.</p> </li> <li> <p> <code>LE</code>: Less than or equal to.</p> </li> <li> <p> <code>EQ</code>: Equal to.</p> </li> <li> <p> <code>NE</code>: Not equal to.</p> </li> </ul>"""
    field_value: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The value provided for comparison on the crawl field. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlsFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_glue.types.field_name

        out["FieldName"] = aws_sdk_glue.types.field_name.serialize_aws_json_1_1(
            value["field_name"]
        )
    if "filter_operator" in value:
        import aws_sdk_glue.types.filter_operator

        out["FilterOperator"] = (
            aws_sdk_glue.types.filter_operator.serialize_aws_json_1_1(
                value["filter_operator"]
            )
        )
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlsFilter:
    out: CrawlsFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_glue.types.field_name

        out["field_name"] = aws_sdk_glue.types.field_name.deserialize_aws_json_1_1(
            data["FieldName"]
        )
    if "FilterOperator" in data:
        import aws_sdk_glue.types.filter_operator

        out["filter_operator"] = (
            aws_sdk_glue.types.filter_operator.deserialize_aws_json_1_1(
                data["FilterOperator"]
            )
        )
    if "FieldValue" in data:
        out["field_value"] = data["FieldValue"]
    return out
