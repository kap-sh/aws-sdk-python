"""Generated from Smithy shape ``com.amazonaws.lambda#GetProvisionedConcurrencyConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.non_negative_integer
    import aws_sdk_lambda.types.positive_integer
    import aws_sdk_lambda.types.provisioned_concurrency_status_enum
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.timestamp


class GetProvisionedConcurrencyConfigResponse(TypedDict):
    requested_provisioned_concurrent_executions: NotRequired[
        "aws_sdk_lambda.types.positive_integer.PositiveInteger"
    ]
    """<p>The amount of provisioned concurrency requested.</p>"""
    available_provisioned_concurrent_executions: NotRequired[
        "aws_sdk_lambda.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>The amount of provisioned concurrency available.</p>"""
    allocated_provisioned_concurrent_executions: NotRequired[
        "aws_sdk_lambda.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>The amount of provisioned concurrency allocated. When a weighted alias is used during linear and canary deployments, this value fluctuates depending on the amount of concurrency that is provisioned for the function versions.</p>"""
    status: NotRequired[
        "aws_sdk_lambda.types.provisioned_concurrency_status_enum.ProvisionedConcurrencyStatusEnum"
    ]
    """<p>The status of the allocation process.</p>"""
    status_reason: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>For failed allocations, the reason that provisioned concurrency could not be allocated.</p>"""
    last_modified: NotRequired["aws_sdk_lambda.types.timestamp.Timestamp"]
    """<p>The date and time that a user last updated the configuration, in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601 format</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProvisionedConcurrencyConfigResponse) -> dict:
    out: dict = {}
    if "requested_provisioned_concurrent_executions" in value:
        out["RequestedProvisionedConcurrentExecutions"] = value[
            "requested_provisioned_concurrent_executions"
        ]
    if "available_provisioned_concurrent_executions" in value:
        out["AvailableProvisionedConcurrentExecutions"] = value[
            "available_provisioned_concurrent_executions"
        ]
    if "allocated_provisioned_concurrent_executions" in value:
        out["AllocatedProvisionedConcurrentExecutions"] = value[
            "allocated_provisioned_concurrent_executions"
        ]
    if "status" in value:
        import aws_sdk_lambda.types.provisioned_concurrency_status_enum

        out["Status"] = (
            aws_sdk_lambda.types.provisioned_concurrency_status_enum.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> GetProvisionedConcurrencyConfigResponse:
    out: GetProvisionedConcurrencyConfigResponse = {}  # type: ignore[typeddict-item]
    if "RequestedProvisionedConcurrentExecutions" in data:
        out["requested_provisioned_concurrent_executions"] = data[
            "RequestedProvisionedConcurrentExecutions"
        ]
    if "AvailableProvisionedConcurrentExecutions" in data:
        out["available_provisioned_concurrent_executions"] = data[
            "AvailableProvisionedConcurrentExecutions"
        ]
    if "AllocatedProvisionedConcurrentExecutions" in data:
        out["allocated_provisioned_concurrent_executions"] = data[
            "AllocatedProvisionedConcurrentExecutions"
        ]
    if "Status" in data:
        import aws_sdk_lambda.types.provisioned_concurrency_status_enum

        out["status"] = (
            aws_sdk_lambda.types.provisioned_concurrency_status_enum.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    return out
