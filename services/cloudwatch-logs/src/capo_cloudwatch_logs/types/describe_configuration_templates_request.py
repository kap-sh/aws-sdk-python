"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeConfigurationTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_types
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.log_types
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.resource_types
    import capo_cloudwatch_logs.types.service


class DescribeConfigurationTemplatesRequest(TypedDict, closed=True):
    service: NotRequired["capo_cloudwatch_logs.types.service.Service"]
    """<p>Use this parameter to filter the response to include only the configuration templates that apply to the Amazon Web Services service that you specify here.</p>"""
    log_types: NotRequired["capo_cloudwatch_logs.types.log_types.LogTypes"]
    """<p>Use this parameter to filter the response to include only the configuration templates that apply to the log types that you specify here.</p>"""
    resource_types: NotRequired[
        "capo_cloudwatch_logs.types.resource_types.ResourceTypes"
    ]
    """<p>Use this parameter to filter the response to include only the configuration templates that apply to the resource types that you specify here.</p>"""
    delivery_destination_types: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_types.DeliveryDestinationTypes"
    ]
    """<p>Use this parameter to filter the response to include only the configuration templates that apply to the delivery destination types that you specify here.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Use this parameter to limit the number of configuration templates that are returned in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationTemplatesRequest) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "log_types" in value:
        import capo_cloudwatch_logs.types.log_types

        out["logTypes"] = capo_cloudwatch_logs.types.log_types.serialize_aws_json_1_1(
            value["log_types"]
        )
    if "resource_types" in value:
        import capo_cloudwatch_logs.types.resource_types

        out["resourceTypes"] = (
            capo_cloudwatch_logs.types.resource_types.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    if "delivery_destination_types" in value:
        import capo_cloudwatch_logs.types.delivery_destination_types

        out["deliveryDestinationTypes"] = (
            capo_cloudwatch_logs.types.delivery_destination_types.serialize_aws_json_1_1(
                value["delivery_destination_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationTemplatesRequest:
    out: DescribeConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "service" in data:
        out["service"] = data["service"]
    if "logTypes" in data:
        import capo_cloudwatch_logs.types.log_types

        out["log_types"] = (
            capo_cloudwatch_logs.types.log_types.deserialize_aws_json_1_1(
                data["logTypes"]
            )
        )
    if "resourceTypes" in data:
        import capo_cloudwatch_logs.types.resource_types

        out["resource_types"] = (
            capo_cloudwatch_logs.types.resource_types.deserialize_aws_json_1_1(
                data["resourceTypes"]
            )
        )
    if "deliveryDestinationTypes" in data:
        import capo_cloudwatch_logs.types.delivery_destination_types

        out["delivery_destination_types"] = (
            capo_cloudwatch_logs.types.delivery_destination_types.deserialize_aws_json_1_1(
                data["deliveryDestinationTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
