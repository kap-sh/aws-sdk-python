"""Generated from Smithy shape ``com.amazonaws.osis#RevokePipelineEndpointConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.pipeline_endpoint_ids_list


class RevokePipelineEndpointConnectionsRequest(TypedDict, closed=True):
    pipeline_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the pipeline from which to revoke endpoint connections.</p>"""
    endpoint_ids: (
        "aws_sdk_osis.types.pipeline_endpoint_ids_list.PipelineEndpointIdsList"
    )
    """<p>A list of endpoint IDs for which to revoke access to the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokePipelineEndpointConnectionsRequest) -> dict:
    out: dict = {}
    out["PipelineArn"] = value["pipeline_arn"]
    import aws_sdk_osis.types.pipeline_endpoint_ids_list

    out["EndpointIds"] = aws_sdk_osis.types.pipeline_endpoint_ids_list.serialize_json(
        value["endpoint_ids"]
    )
    return out


def deserialize_json(data: dict) -> RevokePipelineEndpointConnectionsRequest:
    out: RevokePipelineEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    else:
        raise DeserializationError(
            "RevokePipelineEndpointConnectionsRequest.pipeline_arn required"
        )
    if "EndpointIds" in data:
        import aws_sdk_osis.types.pipeline_endpoint_ids_list

        out["endpoint_ids"] = (
            aws_sdk_osis.types.pipeline_endpoint_ids_list.deserialize_json(
                data["EndpointIds"]
            )
        )
    else:
        raise DeserializationError(
            "RevokePipelineEndpointConnectionsRequest.endpoint_ids required"
        )
    return out
