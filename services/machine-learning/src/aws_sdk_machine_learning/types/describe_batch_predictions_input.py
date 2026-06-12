"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeBatchPredictionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.batch_prediction_filter_variable
    import aws_sdk_machine_learning.types.comparator_value
    import aws_sdk_machine_learning.types.page_limit
    import aws_sdk_machine_learning.types.sort_order
    import aws_sdk_machine_learning.types.string_type


class DescribeBatchPredictionsInput(TypedDict):
    filter_variable: NotRequired[
        "aws_sdk_machine_learning.types.batch_prediction_filter_variable.BatchPredictionFilterVariable"
    ]
    """<p>Use one of the following variables to filter a list of <code>BatchPrediction</code>:</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to the <code>BatchPrediction</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to the <code>BatchPrediction</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of the <code>BatchPrediction</code> <b> </b> <code>Name</code>.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked the <code>BatchPrediction</code> creation.</p> </li> <li> <p> <code>MLModelId</code> - Sets the search criteria to the <code>MLModel</code> used in the <code>BatchPrediction</code>.</p> </li> <li> <p> <code>DataSourceId</code> - Sets the search criteria to the <code>DataSource</code> used in the <code>BatchPrediction</code>.</p> </li> <li> <p> <code>DataURI</code> - Sets the search criteria to the data file(s) used in the <code>BatchPrediction</code>. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.</p> </li> </ul>"""
    eq: NotRequired["aws_sdk_machine_learning.types.comparator_value.ComparatorValue"]
    """<p>The equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that exactly match the value specified with <code>EQ</code>.</p>"""
    gt: NotRequired["aws_sdk_machine_learning.types.comparator_value.ComparatorValue"]
    """<p>The greater than operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are greater than the value specified with <code>GT</code>.</p>"""
    lt: NotRequired["aws_sdk_machine_learning.types.comparator_value.ComparatorValue"]
    """<p>The less than operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are less than the value specified with <code>LT</code>.</p>"""
    ge: NotRequired["aws_sdk_machine_learning.types.comparator_value.ComparatorValue"]
    """<p>The greater than or equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are greater than or equal to the value specified with <code>GE</code>. </p>"""
    le: NotRequired["aws_sdk_machine_learning.types.comparator_value.ComparatorValue"]
    """<p>The less than or equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values that are less than or equal to the value specified with <code>LE</code>.</p>"""
    ne: NotRequired["aws_sdk_machine_learning.types.comparator_value.ComparatorValue"]
    """<p>The not equal to operator. The <code>BatchPrediction</code> results will have <code>FilterVariable</code> values not equal to the value specified with <code>NE</code>.</p>"""
    prefix: NotRequired[
        "aws_sdk_machine_learning.types.comparator_value.ComparatorValue"
    ]
    """<p>A string that is found at the beginning of a variable, such as <code>Name</code> or <code>Id</code>.</p> <p>For example, a <code>Batch Prediction</code> operation could have the <code>Name</code> <code>2014-09-09-HolidayGiftMailer</code>. To search for this <code>BatchPrediction</code>, select <code>Name</code> for the <code>FilterVariable</code> and any of the following strings for the <code>Prefix</code>: </p> <ul> <li> <p>2014-09</p> </li> <li> <p>2014-09-09</p> </li> <li> <p>2014-09-09-Holiday</p> </li> </ul>"""
    sort_order: NotRequired["aws_sdk_machine_learning.types.sort_order.SortOrder"]
    """<p>A two-value parameter that determines the sequence of the resulting list of <code>MLModel</code>s.</p> <ul> <li> <p> <code>asc</code> - Arranges the list in ascending order (A-Z, 0-9).</p> </li> <li> <p> <code>dsc</code> - Arranges the list in descending order (Z-A, 9-0).</p> </li> </ul> <p>Results are sorted by <code>FilterVariable</code>.</p>"""
    next_token: NotRequired["aws_sdk_machine_learning.types.string_type.StringType"]
    """<p>An ID of the page in the paginated results.</p>"""
    limit: NotRequired["aws_sdk_machine_learning.types.page_limit.PageLimit"]
    """<p>The number of pages of information to include in the result. The range of acceptable values is <code>1</code> through <code>100</code>. The default value is <code>100</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchPredictionsInput) -> dict:
    out: dict = {}
    if "filter_variable" in value:
        import aws_sdk_machine_learning.types.batch_prediction_filter_variable

        out["FilterVariable"] = (
            aws_sdk_machine_learning.types.batch_prediction_filter_variable.serialize_aws_json_1_1(
                value["filter_variable"]
            )
        )
    if "eq" in value:
        out["EQ"] = value["eq"]
    if "gt" in value:
        out["GT"] = value["gt"]
    if "lt" in value:
        out["LT"] = value["lt"]
    if "ge" in value:
        out["GE"] = value["ge"]
    if "le" in value:
        out["LE"] = value["le"]
    if "ne" in value:
        out["NE"] = value["ne"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "sort_order" in value:
        import aws_sdk_machine_learning.types.sort_order

        out["SortOrder"] = (
            aws_sdk_machine_learning.types.sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchPredictionsInput:
    out: DescribeBatchPredictionsInput = {}  # type: ignore[typeddict-item]
    if "FilterVariable" in data:
        import aws_sdk_machine_learning.types.batch_prediction_filter_variable

        out["filter_variable"] = (
            aws_sdk_machine_learning.types.batch_prediction_filter_variable.deserialize_aws_json_1_1(
                data["FilterVariable"]
            )
        )
    if "EQ" in data:
        out["eq"] = data["EQ"]
    if "GT" in data:
        out["gt"] = data["GT"]
    if "LT" in data:
        out["lt"] = data["LT"]
    if "GE" in data:
        out["ge"] = data["GE"]
    if "LE" in data:
        out["le"] = data["LE"]
    if "NE" in data:
        out["ne"] = data["NE"]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "SortOrder" in data:
        import aws_sdk_machine_learning.types.sort_order

        out["sort_order"] = (
            aws_sdk_machine_learning.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
