"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSetRefreshPropertiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_refresh_properties
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeDataSetRefreshPropertiesResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    data_set_refresh_properties: NotRequired[
        "aws_sdk_quicksight.types.data_set_refresh_properties.DataSetRefreshProperties"
    ]
    """<p>The dataset refresh properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSetRefreshPropertiesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "data_set_refresh_properties" in value:
        import aws_sdk_quicksight.types.data_set_refresh_properties

        out["DataSetRefreshProperties"] = (
            aws_sdk_quicksight.types.data_set_refresh_properties.serialize_json(
                value["data_set_refresh_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDataSetRefreshPropertiesResponse:
    out: DescribeDataSetRefreshPropertiesResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "DataSetRefreshProperties" in data:
        import aws_sdk_quicksight.types.data_set_refresh_properties

        out["data_set_refresh_properties"] = (
            aws_sdk_quicksight.types.data_set_refresh_properties.deserialize_json(
                data["DataSetRefreshProperties"]
            )
        )
    return out
