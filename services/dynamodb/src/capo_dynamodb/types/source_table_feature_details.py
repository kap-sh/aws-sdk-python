"""Generated from Smithy shape ``com.amazonaws.dynamodb#SourceTableFeatureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.global_secondary_indexes
    import capo_dynamodb.types.local_secondary_indexes
    import capo_dynamodb.types.sse_description
    import capo_dynamodb.types.stream_specification
    import capo_dynamodb.types.time_to_live_description


class SourceTableFeatureDetails(TypedDict, closed=True):
    local_secondary_indexes: NotRequired[
        "capo_dynamodb.types.local_secondary_indexes.LocalSecondaryIndexes"
    ]
    """<p>Represents the LSI properties for the table when the backup was created. It includes the IndexName, KeySchema and Projection for the LSIs on the table at the time of backup. </p>"""
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.global_secondary_indexes.GlobalSecondaryIndexes"
    ]
    """<p>Represents the GSI properties for the table when the backup was created. It includes the IndexName, KeySchema, Projection, and ProvisionedThroughput for the GSIs on the table at the time of backup. </p>"""
    stream_description: NotRequired[
        "capo_dynamodb.types.stream_specification.StreamSpecification"
    ]
    """<p>Stream settings on the table when the backup was created.</p>"""
    time_to_live_description: NotRequired[
        "capo_dynamodb.types.time_to_live_description.TimeToLiveDescription"
    ]
    """<p>Time to Live settings on the table when the backup was created.</p>"""
    sse_description: NotRequired["capo_dynamodb.types.sse_description.SSEDescription"]
    """<p>The description of the server-side encryption status on the table when the backup was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceTableFeatureDetails) -> dict:
    out: dict = {}
    if "local_secondary_indexes" in value:
        import capo_dynamodb.types.local_secondary_indexes

        out["LocalSecondaryIndexes"] = (
            capo_dynamodb.types.local_secondary_indexes.serialize_aws_json_1_0(
                value["local_secondary_indexes"]
            )
        )
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.global_secondary_indexes

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.global_secondary_indexes.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    if "stream_description" in value:
        import capo_dynamodb.types.stream_specification

        out["StreamDescription"] = (
            capo_dynamodb.types.stream_specification.serialize_aws_json_1_0(
                value["stream_description"]
            )
        )
    if "time_to_live_description" in value:
        import capo_dynamodb.types.time_to_live_description

        out["TimeToLiveDescription"] = (
            capo_dynamodb.types.time_to_live_description.serialize_aws_json_1_0(
                value["time_to_live_description"]
            )
        )
    if "sse_description" in value:
        import capo_dynamodb.types.sse_description

        out["SSEDescription"] = (
            capo_dynamodb.types.sse_description.serialize_aws_json_1_0(
                value["sse_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceTableFeatureDetails:
    out: SourceTableFeatureDetails = {}  # type: ignore[typeddict-item]
    if "LocalSecondaryIndexes" in data:
        import capo_dynamodb.types.local_secondary_indexes

        out["local_secondary_indexes"] = (
            capo_dynamodb.types.local_secondary_indexes.deserialize_aws_json_1_0(
                data["LocalSecondaryIndexes"]
            )
        )
    if "GlobalSecondaryIndexes" in data:
        import capo_dynamodb.types.global_secondary_indexes

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.global_secondary_indexes.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    if "StreamDescription" in data:
        import capo_dynamodb.types.stream_specification

        out["stream_description"] = (
            capo_dynamodb.types.stream_specification.deserialize_aws_json_1_0(
                data["StreamDescription"]
            )
        )
    if "TimeToLiveDescription" in data:
        import capo_dynamodb.types.time_to_live_description

        out["time_to_live_description"] = (
            capo_dynamodb.types.time_to_live_description.deserialize_aws_json_1_0(
                data["TimeToLiveDescription"]
            )
        )
    if "SSEDescription" in data:
        import capo_dynamodb.types.sse_description

        out["sse_description"] = (
            capo_dynamodb.types.sse_description.deserialize_aws_json_1_0(
                data["SSEDescription"]
            )
        )
    return out
