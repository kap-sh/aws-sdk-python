"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaLayerAggregationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.severity_counts


class LambdaLayerAggregationResponse(TypedDict):
    function_name: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The names of the Amazon Web Services Lambda functions associated with the layers.</p>"""
    resource_id: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The Resource ID of the Amazon Web Services Lambda function layer.</p>"""
    layer_arn: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function layer.</p>"""
    account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The account ID of the Amazon Web Services Lambda function layer.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    """<p>An object that contains the counts of aggregated finding per severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaLayerAggregationResponse) -> dict:
    out: dict = {}
    out["functionName"] = value["function_name"]
    out["resourceId"] = value["resource_id"]
    out["layerArn"] = value["layer_arn"]
    out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> LambdaLayerAggregationResponse:
    out: LambdaLayerAggregationResponse = {}  # type: ignore[typeddict-item]
    if "functionName" in data:
        out["function_name"] = data["functionName"]
    else:
        raise DeserializationError(
            "LambdaLayerAggregationResponse.function_name required"
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "LambdaLayerAggregationResponse.resource_id required"
        )
    if "layerArn" in data:
        out["layer_arn"] = data["layerArn"]
    else:
        raise DeserializationError("LambdaLayerAggregationResponse.layer_arn required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("LambdaLayerAggregationResponse.account_id required")
    if "severityCounts" in data:
        import aws_sdk_inspector2.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_inspector2.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    return out
