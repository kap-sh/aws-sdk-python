"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.operation


class GetOperationResponse(TypedDict, closed=True):
    operation: NotRequired["aws_sdk_servicediscovery.types.operation.Operation"]
    """<p>A complex type that contains information about the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationResponse) -> dict:
    out: dict = {}
    if "operation" in value:
        import aws_sdk_servicediscovery.types.operation

        out["Operation"] = (
            aws_sdk_servicediscovery.types.operation.serialize_aws_json_1_1(
                value["operation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationResponse:
    out: GetOperationResponse = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        import aws_sdk_servicediscovery.types.operation

        out["operation"] = (
            aws_sdk_servicediscovery.types.operation.deserialize_aws_json_1_1(
                data["Operation"]
            )
        )
    return out
