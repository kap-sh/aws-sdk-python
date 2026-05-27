"""Generated from Smithy shape ``com.amazonaws.dynamodb#Projection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.non_key_attribute_name_list
    import aws_sdk_dynamodb.types.projection_type


class Projection(TypedDict):
    projection_type: NotRequired[
        "aws_sdk_dynamodb.types.projection_type.ProjectionType"
    ]
    """<p>The set of attributes that are projected into the index:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - In addition to the attributes described in <code>KEYS_ONLY</code>, the secondary index will include other non-key attributes that you specify.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> <p>When using the DynamoDB console, <code>ALL</code> is selected by default.</p>"""
    non_key_attributes: NotRequired[
        "aws_sdk_dynamodb.types.non_key_attribute_name_list.NonKeyAttributeNameList"
    ]
    """<p>Represents the non-key attribute names which will be projected into the index.</p> <p>For global and local secondary indexes, the total count of <code>NonKeyAttributes</code> summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p>"""
