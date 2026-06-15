"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListVehiclesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.attribute_names_list
    import aws_sdk_iotfleetwise.types.attribute_values_list
    import aws_sdk_iotfleetwise.types.list_response_scope
    import aws_sdk_iotfleetwise.types.list_vehicles_max_results
    import aws_sdk_iotfleetwise.types.next_token


class ListVehiclesRequest(TypedDict):
    model_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The Amazon Resource Name (ARN) of a vehicle model (model manifest). You can use this optional parameter to list only the vehicles created from a certain vehicle model. </p>"""
    attribute_names: NotRequired[
        "aws_sdk_iotfleetwise.types.attribute_names_list.attributeNamesList"
    ]
    r"""<p>The fully qualified names of the attributes. You can use this optional parameter to list the vehicles containing all the attributes in the request. For example, <code>attributeNames</code> could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\" and the corresponding <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" . In this case, the API will filter vehicles with an attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filters to return the subset of vehicles that match the attributes filter condition.</p>"""
    attribute_values: NotRequired[
        "aws_sdk_iotfleetwise.types.attribute_values_list.attributeValuesList"
    ]
    r"""<p>Static information about a vehicle attribute value in string format. You can use this optional parameter in conjunction with <code>attributeNames</code> to list the vehicles containing all the <code>attributeValues</code> corresponding to the <code>attributeNames</code> filter. For example, <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" and the corresponding <code>attributeNames</code> filter could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\". In this case, the API will filter vehicles with attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filter to return the subset of vehicles that match the attributes filter condition.</p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired[
        "aws_sdk_iotfleetwise.types.list_vehicles_max_results.listVehiclesMaxResults"
    ]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    list_response_scope: NotRequired[
        "aws_sdk_iotfleetwise.types.list_response_scope.ListResponseScope"
    ]
    """<p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: vehicle name, Amazon Resource Name (ARN), creation time, and last modification time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVehiclesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVehiclesRequest:
    out: ListVehiclesRequest = {}  # type: ignore[typeddict-item]
    return out
