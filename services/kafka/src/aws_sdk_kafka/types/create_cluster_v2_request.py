"""Generated from Smithy shape ``com.amazonaws.kafka#CreateClusterV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__map_of__string
    import aws_sdk_kafka.types.__string_min1_max64
    import aws_sdk_kafka.types.provisioned_request
    import aws_sdk_kafka.types.serverless_request


class CreateClusterV2Request(TypedDict):
    cluster_name: NotRequired[
        "aws_sdk_kafka.types.__string_min1_max64.__stringMin1Max64"
    ]
    """<p>The name of the cluster.</p>"""
    tags: NotRequired["aws_sdk_kafka.types.__map_of__string.__mapOf__string"]
    """<p>A map of tags that you want the cluster to have.</p>"""
    provisioned: NotRequired[
        "aws_sdk_kafka.types.provisioned_request.ProvisionedRequest"
    ]
    """<p>Information about the provisioned cluster.</p>"""
    serverless: NotRequired["aws_sdk_kafka.types.serverless_request.ServerlessRequest"]
    """<p>Information about the serverless cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterV2Request) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "tags" in value:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "provisioned" in value:
        import aws_sdk_kafka.types.provisioned_request

        out["provisioned"] = aws_sdk_kafka.types.provisioned_request.serialize_json(
            value["provisioned"]
        )
    if "serverless" in value:
        import aws_sdk_kafka.types.serverless_request

        out["serverless"] = aws_sdk_kafka.types.serverless_request.serialize_json(
            value["serverless"]
        )
    return out


def deserialize_json(data: dict) -> CreateClusterV2Request:
    out: CreateClusterV2Request = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "tags" in data:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if "provisioned" in data:
        import aws_sdk_kafka.types.provisioned_request

        out["provisioned"] = aws_sdk_kafka.types.provisioned_request.deserialize_json(
            data["provisioned"]
        )
    if "serverless" in data:
        import aws_sdk_kafka.types.serverless_request

        out["serverless"] = aws_sdk_kafka.types.serverless_request.deserialize_json(
            data["serverless"]
        )
    return out
