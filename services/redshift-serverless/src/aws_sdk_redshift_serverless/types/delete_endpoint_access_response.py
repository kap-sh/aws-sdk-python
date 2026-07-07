"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.endpoint_access


class DeleteEndpointAccessResponse(TypedDict, closed=True):
    endpoint: NotRequired[
        "aws_sdk_redshift_serverless.types.endpoint_access.EndpointAccess"
    ]
    """<p>The deleted VPC endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointAccessResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import aws_sdk_redshift_serverless.types.endpoint_access

        out["endpoint"] = (
            aws_sdk_redshift_serverless.types.endpoint_access.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointAccessResponse:
    out: DeleteEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        import aws_sdk_redshift_serverless.types.endpoint_access

        out["endpoint"] = (
            aws_sdk_redshift_serverless.types.endpoint_access.deserialize_aws_json_1_1(
                data["endpoint"]
            )
        )
    return out
