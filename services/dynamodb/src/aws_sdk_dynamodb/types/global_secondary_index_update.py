"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.create_global_secondary_index_action
    import aws_sdk_dynamodb.types.delete_global_secondary_index_action
    import aws_sdk_dynamodb.types.update_global_secondary_index_action


class GlobalSecondaryIndexUpdate(TypedDict):
    update: NotRequired[
        "aws_sdk_dynamodb.types.update_global_secondary_index_action.UpdateGlobalSecondaryIndexAction"
    ]
    """<p>The name of an existing global secondary index, along with new provisioned throughput settings to be applied to that index.</p>"""
    create: NotRequired[
        "aws_sdk_dynamodb.types.create_global_secondary_index_action.CreateGlobalSecondaryIndexAction"
    ]
    """<p>The parameters required for creating a global secondary index on an existing table:</p> <ul> <li> <p> <code>IndexName </code> </p> </li> <li> <p> <code>KeySchema </code> </p> </li> <li> <p> <code>AttributeDefinitions </code> </p> </li> <li> <p> <code>Projection </code> </p> </li> <li> <p> <code>ProvisionedThroughput </code> </p> </li> </ul>"""
    delete: NotRequired[
        "aws_sdk_dynamodb.types.delete_global_secondary_index_action.DeleteGlobalSecondaryIndexAction"
    ]
    """<p>The name of an existing global secondary index to be removed.</p>"""
