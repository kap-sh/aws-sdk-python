"""Generated from Smithy shape ``com.amazonaws.apprunner#ListVpcIngressConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.next_token
    import aws_sdk_apprunner.types.vpc_ingress_connection_summary_list


class ListVpcIngressConnectionsResponse(TypedDict, closed=True):
    vpc_ingress_connection_summary_list: "aws_sdk_apprunner.types.vpc_ingress_connection_summary_list.VpcIngressConnectionSummaryList"
    """<p>A list of summary information records for VPC Ingress Connections. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcIngressConnectionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.vpc_ingress_connection_summary_list

    out["VpcIngressConnectionSummaryList"] = (
        aws_sdk_apprunner.types.vpc_ingress_connection_summary_list.serialize_aws_json_1_0(
            value["vpc_ingress_connection_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcIngressConnectionsResponse:
    out: ListVpcIngressConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnectionSummaryList" in data:
        import aws_sdk_apprunner.types.vpc_ingress_connection_summary_list

        out["vpc_ingress_connection_summary_list"] = (
            aws_sdk_apprunner.types.vpc_ingress_connection_summary_list.deserialize_aws_json_1_0(
                data["VpcIngressConnectionSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListVpcIngressConnectionsResponse.vpc_ingress_connection_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
