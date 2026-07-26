"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.endpoint_access


class CreateEndpointAccessResponse(TypedDict, closed=True):
    endpoint: NotRequired[
        "capo_redshift_serverless.types.endpoint_access.EndpointAccess"
    ]
    """<p>The created VPC endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointAccessResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import capo_redshift_serverless.types.endpoint_access

        out["endpoint"] = (
            capo_redshift_serverless.types.endpoint_access.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointAccessResponse:
    out: CreateEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        import capo_redshift_serverless.types.endpoint_access

        out["endpoint"] = (
            capo_redshift_serverless.types.endpoint_access.deserialize_aws_json_1_1(
                data["endpoint"]
            )
        )
    return out
