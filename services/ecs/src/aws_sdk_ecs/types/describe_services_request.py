"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_field_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class DescribeServicesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.</p>"""
    services: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of services to describe. You may specify up to 10 services to describe in a single operation.</p>"""
    include: NotRequired["aws_sdk_ecs.types.service_field_list.ServiceFieldList"]
    """<p>Determines whether you want to see the resource tags for the service. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import aws_sdk_ecs.types.string_list

    out["services"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["services"]
    )
    if "include" in value:
        import aws_sdk_ecs.types.service_field_list

        out["include"] = aws_sdk_ecs.types.service_field_list.serialize_aws_json_1_1(
            value["include"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesRequest:
    out: DescribeServicesRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "services" in data:
        import aws_sdk_ecs.types.string_list

        out["services"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["services"]
        )
    else:
        raise DeserializationError("DescribeServicesRequest.services required")
    if "include" in data:
        import aws_sdk_ecs.types.service_field_list

        out["include"] = aws_sdk_ecs.types.service_field_list.deserialize_aws_json_1_1(
            data["include"]
        )
    return out
